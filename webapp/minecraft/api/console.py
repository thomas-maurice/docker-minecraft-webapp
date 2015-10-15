# -*- coding: utf8 -*-

# Copyright (C) 2015 Thomas Maurice <thomas@maurice.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins, serializers, generics, status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from lib import mcrcon
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

class CannotConnectException(APIException):
    status_code = 503
    default_detail = 'Could not connect to console :/ try again later.'

class ConsoleSerializer(serializers.Serializer):
    command = serializers.CharField(required=True)
    response = serializers.CharField(read_only=True)

class Console(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
        Controls console via the API
    """
    serializer_class = ConsoleSerializer
    def post(self, request, *args, **kwargs):
        serializer = ConsoleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        resp = {"command": serializer.data['command']}
        console = mcrcon.MCRcon()
        try:
            pwfile = open(settings.CONFIG_HOME + "/rcon_password", "r")
            pw = pwfile.read().strip()
            pwfile.close()
            console.connect("localhost", 25566)
            console.login(pw)
            resp['response'] = console.command(serializer.data['command'])
            return Response(ConsoleSerializer(resp).data)
        except Exception as exce:
            raise CannotConnectException(str(exce))
