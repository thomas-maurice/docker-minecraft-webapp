from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import supervisor.xmlrpc
import xmlrpclib

@login_required()
def system(request):
    try:
        p = xmlrpclib.ServerProxy('http://127.0.0.1',
                transport=supervisor.xmlrpc.SupervisorTransport(
                    None, None,
                    'unix:///var/run/supervisor.sock'))
        programs = p.supervisor.getAllProcessInfo()
        return render(request, 'system.html', {"programs": programs, "failure": False})
    except:
        return render(request, 'system.html', {"failure": True})
