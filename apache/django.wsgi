import os
import sys

path = '/home/django/source/bhp056/bhp056'.format(root_dir)
if path not in sys.path: sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bhp056.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
