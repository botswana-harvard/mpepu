import platform
import sys
from os.path import realpath, abspath, join, dirname

from unipath import Path

from bhp056.config import LOGGING

from bhp056.config import *


ADMINS = (('erikvw', 'ew@2789@gmail.com'),)

# Path
SETTINGS_DIR = dirname(realpath(__file__))
SOURCE_DIR = Path(__file__).ancestor(4)
PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child('media')
STATIC_ROOT = PROJECT_DIR.child('static')
TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
    PROJECT_DIR.child('edc', 'lab', 'lab_clinic_api', 'templates'),
)
STATICFILES_DIRS = ()
CONFIG_DIR = PROJECT_DIR.child('bhp056')
MAP_DIR = STATIC_ROOT.child('img')
DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'

#Email configuration
SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = 'edcdev@bhp.org.bw'
EMAIL_SUBJECT_PREFIX = '[mpepu] '
DEFAULT_FROM_EMAIL = 'edcdev@bhp.org.bw'
ADMINS = (
    ('erikvw', 'ew2789@gmail.com'),
    ('fchilisa', 'fchilisa@bhp.org.bw'),
    ('twicet', 'ttshwenyane@bhp.org.bw'),
    ('mkewagamang', 'mkewagamang@bhp.org.bw'),
)


MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', 's007', 's007.bhp.org.bw', '192.168.1.50']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Gaborone'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#langauage setting
ugettext = lambda s: s

#LOCALE_PATHS = ('locale', )

LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# A list of locations of additional static files
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'dajaxice.finders.DajaxiceFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0$q&@p=jz(+_r^+phzenyqi49#y2^3ot3h#jru+32z&+cm&j51'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
     'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
     )),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")

ROOT_URLCONF = 'bhp056.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'django_databrowse',
    #'dajaxice',
    'dajax',
    'south',

    'edc.apps.admin_supplemental_fields',
    'edc.apps.app_configuration',

    'edc.audit',

    'edc.base.modeladmin',
    'edc.base.form',
    'edc.base.model',

    'edc.core.identifier',
    'edc.core.crypto_fields',
    'edc.core.model_data_inspector',
    'edc.core.model_selector',
    'edc.core.bhp_templates',
    'edc.core.bhp_static',
    'edc.core.bhp_string',
    'edc.core.bhp_userprofile',
    'edc.core.bhp_poll_mysql',
    'edc.core.bhp_templatetags',
    'edc.core.bhp_common',
    'edc.core.bhp_content_type_map',
    'edc.core.bhp_data_manager',
    'edc.core.bhp_variables',
    'edc.core.bhp_site_edc',
    'edc.core.bhp_nmap',
    'edc.core.bhp_context',
    'edc.core.bhp_using',
    'edc.core.bhp_export_data',
    'edc.core.bhp_birt_reports',

    'edc.dashboard.base',
    'edc.dashboard.search',
    'edc.dashboard.subject',
    'edc.dashboard.section',

    'edc.export',
    'edc.import',
    'edc.entry_meta_data',

    'edc.data_dictionary',

    'edc.map',

    'edc.testing',

    'edc.subject.lab_tracker',
    'edc.subject.code_lists',
    'edc.subject.rule_groups',
    'edc.subject.actg',
    'edc.subject.entry',
    'edc.subject.consent',
    'edc.subject.contact',
    'edc.subject.locator',
    'edc.subject.subject_summary',
    'edc.subject.off_study',
    'edc.subject.registration',
    'edc.subject.appointment',
    'edc.subject.appointment_helper',
    'edc.subject.visit_schedule',
    'edc.subject.visit_tracking',
    'edc.subject.appointment',
    'edc.subject.subject',
    'edc.subject.subject_config',
    'edc.subject.adverse_event',

    'edc.lab.lab_clinic_api',
    'edc.lab.lab_clinic_reference',
    'edc.lab.lab_requisition',
    'edc.lab.lab_packing',
    'edc.pharma.dispenser',

    'lis.core.lab_common',
    'lis.core.lab_flag',
    'lis.core.lab_grading',
    'lis.core.lab_reference',
    'lis.core.lab_result_report',
    'lis.core.bhp_research_protocol',
    'lis.core.lock',

    'lis.specimen.lab_aliquot_list',
    'lis.specimen.lab_panel',
    'lis.specimen.lab_test_code',
    'lis.specimen.lab_receive',
    'lis.specimen.lab_aliquot',
    'lis.specimen.lab_order',
    'lis.specimen.lab_result',
    'lis.specimen.lab_result_item',

    'lis.subject.lab_account',
    'lis.subject.lab_patient',

    'lis.exim.lab_export',
    'lis.exim.lab_import',
    'lis.exim.lab_import_lis',
    'lis.exim.lab_import_dmis',

    'lis.labeling',

    'apps.mpepu',
    'apps.mpepu_lab',
    'apps.mpepu_list',
    'apps.mpepu_maternal',
    'apps.mpepu_infant',
    'apps.mpepu_infant_rando',
    'apps.mpepu_dashboard',
    'apps.mpepu_stats',
    'apps.mpepu_reference',
    #'tastypie',
)


# django email settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'edcdev'
EMAIL_HOST_PASSWORD = 'cc3721b'
EMAIL_USE_TLS = True
#EMAIL_AFTER_CONSUME = False

SOUTH_LOGGING_FILE = join(dirname(__file__), "south.log")
SOUTH_LOGGING_ON = True
AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"
#DAJAXICE_MEDIA_PREFIX = "dajaxice"

# only for community server
IS_COMMUNITY_SERVER = True
ALLOW_DELETE_MODEL_FROM_SERIALIZATION = False
ALLOW_MODEL_SERIALIZATION = True

# django auth
AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"

# EDC GENERAL SETTINGS
APP_NAME = 'mpepu'
PROJECT_NUMBER = 'BHP056'
PROJECT_IDENTIFIER_PREFIX = '056'
PROJECT_IDENTIFIER_MODULUS = 7
PROJECT_TITLE = 'Mpepu Study'
PROTOCOL_REVISION = ''
INSTITUTION = 'Botswana-Harvard AIDS Institute Partnership'
LOGIN_URL = '/{app_name}/login/'.format(app_name=APP_NAME)
LOGIN_REDIRECT_URL = '/{app_name}/'.format(app_name=APP_NAME)
LOGOUT_URL = '/{app_name}/logout/'.format(app_name=APP_NAME)
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
LAB_LOCK_NAME = 'BHP056'
LABDB = 'bhplab'
SESSION_COOKIE_AGE = 3000
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
DEVICE_ID = '99'
SUBJECT_TYPES = ['infant', 'maternal']
MAX_SUBJECTS = {'maternal': 3274, 'infant': 4500}
APPOINTMENTS_PER_DAY_MAX = 20
APPOINTMENTS_DAYS_FORWARD = 15

SUBJECT_APP_LIST = ['mpepu_infant', 'mpepu_maternal']
DISPATCH_APP_LABELS = []

#BHP_CRYPTO_SETTINGS
IS_SECURE_DEVICE = False
MAY_CREATE_NEW_KEYS = True

FIELD_MAX_LENGTH = 'migration'

# LAB REFERENCE AND GRADING
REFERENCE_RANGE_LIST = 'BHPLAB_NORMAL_RANGES_201005'
GRADING_LIST = 'DAIDS_2004'
# for bhp_import_dmis
if platform.system() == 'Darwin':
    LAB_IMPORT_DMIS_DATA_SOURCE = ('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=192.168.1.141;'
                                   'PORT=1433;UID=sa;PWD=cc3721b;DATABASE=BHPLAB')
else:
    LAB_IMPORT_DMIS_DATA_SOURCE = ('DRIVER={FreeTDS};SERVER=192.168.1.141;UID=sa;PWD=cc3721b;'
                                   'DATABASE=BHPLAB')
VAR_ROOT = '/var'
LOGGING = LOGGING
