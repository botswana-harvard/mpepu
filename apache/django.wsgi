import os
import sys
import platform
#import djcelery
#djcelery.setup_loader()

home_dir = 'home'

path = '/{0}/django/source'.format(home_dir)
if path not in sys.path:
    sys.path.append(path)

path = '/{0}/django/source/bhp066'.format(home_dir)
if path not in sys.path:
    sys.path.append(path)

path = '/{0}/django/source/bhp066/keys'.format(home_dir)
if path not in sys.path:
    sys.path.append(path)
sys.path.insert(0, "/{0}/django/Virtualenvs/django1_5/lib/python2.7/site-packages/".format(home_dir))

os.environ['DJANGO_SETTINGS_MODULE'] = 'bhp066.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

