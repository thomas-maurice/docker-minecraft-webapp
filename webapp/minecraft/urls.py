from django.conf.urls import patterns, url, include
from minecraft.views  import ListUsers, CreateUser, ShowUser, DeleteUser, UpdateUser
from minecraft import api
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', 'minecraft.views.index', name="index"),

    url(r'user/(?P<pk>\d+)$', ShowUser.as_view(), name="show_user"),
    url(r'user/update/(?P<pk>\d+)$', UpdateUser.as_view(), name="update_user"),
    url(r'user/delete/(?P<pk>\d+)$', DeleteUser.as_view(), name="delete_user"),
    url(r'user/create$', CreateUser.as_view(), name="create_user"),
    url(r'users?$', ListUsers.as_view(), name="list_user"),

    url(r'^system/$', 'minecraft.views.system', name="system"),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/service/$', api.ServiceList.as_view()),
    url(r'^api/service/action/$', api.ServiceAction.as_view()),

    url(r'^api/config/$', api.Config.as_view()),
    url(r'^api/console/$', api.Console.as_view()),

    (r'^control/$', login_required(TemplateView.as_view(template_name='control.html'))),
    (r'^console/$', login_required(TemplateView.as_view(template_name='console.html'))),
)
