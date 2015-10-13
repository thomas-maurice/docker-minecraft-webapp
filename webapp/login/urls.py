from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {"template_name": "login/login.html"}, name="login"),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {"template_name": "login/login.html", 'next_page': 'login'},
        name="logout"),
    url(r'^password_change$',
        'django.contrib.auth.views.password_change',
        {"template_name": "login/password_change_form.html", "post_change_redirect": "password_change_done"},
        name="pwchange"),
    url(r'^password_change_done$',
        'django.contrib.auth.views.password_change_done',
        {"template_name": "login/password_change_done.html"},
        name="password_change_done"),
)
