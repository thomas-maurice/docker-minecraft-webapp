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

from django.conf import settings
import supervisor.xmlrpc
import xmlrpclib

def get_proxy():
    return xmlrpclib.ServerProxy('http://127.0.0.1',
            transport=supervisor.xmlrpc.SupervisorTransport(
            None, None,
            settings.SUPERVISOR_URL))

def get_processes_info():
    p = get_proxy()
    return p.supervisor.getAllProcessInfo()

def stop(name):
    p = get_proxy()
    return p.supervisor.stopProcess(name, True)

def start(name):
    p = get_proxy()
    return p.supervisor.startProcess(name, True)

def restart(name):
    p = get_proxy()
    try:
        p.supervisor.stopProcess(name, True)
    except:
        pass
    finally:
        return p.supervisor.startProcess(name, True)
