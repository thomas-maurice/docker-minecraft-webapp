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
from lib import supervisorctl
from django.views.decorators.csrf import ensure_csrf_cookie

class SupervisorUnavailable(APIException):
    status_code = 503
    default_detail = 'Supervisor is temporarily unavailable, try again later.'

class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    statename = serializers.CharField(read_only=True)

class ServiceActionSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    action = serializers.ChoiceField(required=True, choices=(
        ('START', "Start"),
        ('STOP', "Stop"),
        ('RESTART', "Restart"),
    ))

class ServiceList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        try:
            programs = supervisorctl.get_processes_info()
            serializer = ServiceSerializer(programs, many=True)
            return Response(serializer.data)
        except Exception as exce:
            print exce
            raise SupervisorUnavailable()

class ServiceAction(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
        Controls services via the API
    """
    serializer_class = ServiceActionSerializer
    def post(self, request, *args, **kwargs):
        serializer = ServiceActionSerializer(data=request.data)
        if not serializer.is_valid():
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            if serializer.data['action'] == "START":
                print serializer.data
                return Response({"result": supervisorctl.start(serializer.data['name'])})
            elif serializer.data['action'] == "RESTART":
                return Response({"result": supervisorctl.restart(serializer.data['name'])})
            elif serializer.data['action'] == "STOP":
                return Response({"result": supervisorctl.stop(serializer.data['name'])})
        except Exception as exce:
            print exce
            raise SupervisorUnavailable()
