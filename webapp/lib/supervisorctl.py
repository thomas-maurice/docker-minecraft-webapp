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
