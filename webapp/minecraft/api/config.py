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

class ConfigSerializer(serializers.Serializer):
    motd = serializers.CharField()
    max_players = serializers.IntegerField(max_value=20, min_value=1)
    spawn_animals = serializers.BooleanField()
    spawn_monsters = serializers.BooleanField()
    online_mode = serializers.BooleanField()

class Config(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
        Controls configuration via the API
    """
    serializer_class = ConfigSerializer
    def post(self, request, *args, **kwargs):
        serializer = ConfigSerializer(data=request.data)
        if not serializer.is_valid():
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response("")
