import os
import sys
#import platform
 
# for apache use be explicit about the ROOT folder
ROOT = '/home/django'
 
VIRTUALENV_PATH = os.path.join(ROOT, '.virtualenvs/django-1.6')
SOURCE_ROOT_PATH = os.path.join(ROOT, 'source')
LOCAL_PROJECT_RELPATH = 'bhp056_project/bhp056'
 
# update paths to projects
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, LOCAL_PROJECT_RELPATH))
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, 'edc_project'))
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, 'lis_project'))
 
# update path to virtualenv
sys.path.insert(0, os.path.join(VIRTUALENV_PATH, 'local/lib/python2.7/site-packages'))
 
# point django to settings. Note settings file name is custom in this case
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
 
#if platform.system() == 'Darwin':
#        os.environ['PYTHON_EGG_CACHE'] = '/usr/local/pylons/python-eggs'
 
# Activate the virtual env
activate_env=os.path.join(VIRTUALENV_PATH, 'bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

#types {
#    text/html                             html htm shtml;
#    text/css                              css;
#    image/gif                             gif;
#    image/jpeg                            jpeg jpg;
#    application/x-javascript              js;
#}