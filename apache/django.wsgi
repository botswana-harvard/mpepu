import os
import sys

path = '/home/django/source/bhp056/bhp056'
if path not in sys.path: sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bhp056.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
