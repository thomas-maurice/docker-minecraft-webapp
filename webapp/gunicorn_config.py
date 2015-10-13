# -*- coding: utf-8 -*-

# Gunicorn config 

import os

bind = ['127.0.0.1:8081']
workers = 16
reload = True

user = 'minecraft'
