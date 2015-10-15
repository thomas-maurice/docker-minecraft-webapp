from django.conf.urls import patterns, url

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
