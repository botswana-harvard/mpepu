import os
import sys
#import djcelery

#djcelery.setup_loader()

path = '/home/django/source'
if path not in sys.path:
    sys.path.append(path)
 
path = '/home/django/source/bhp062'
if path not in sys.path:
    sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'bhp062.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
