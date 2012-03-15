# Django settings for bhp project.
import os, platform
os.environ['MPLCONFIGDIR']='/tmp'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('erikvw', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': 'bhp056_20120315',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'cc3721b',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'lab_api': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    	'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': 'lab',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'cc3721b',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


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
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/django/source/bhp056/sitestatic/'

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# A list of locations of additional static files
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0$q&@p=jz(+_r^+phzenyqi49#y2^3ot3h#jru+32z&+cm&j51'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")


ROOT_URLCONF = 'bhp056.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'databrowse',
    'django_extensions',
    'dajaxice',
    'dajax',
    'south',
    'audit_trail',
    'autocomplete',
    'bhp_basesite',
    'bhp_userprofile', 
    'bhp_poll_mysql',
    'bhp_model_selector',
    'bhp_templatetags',
    'bhp_calendar',    
    'bhp_actg_reference',
    'bhp_adverse',
    'bhp_haart',    
    'bhp_code_lists',    
    'bhp_common',    
    'bhp_identifier',    
    'bhp_content_type_map',    
    'bhp_search',
    'bhp_consent',
    'bhp_registration',
    'bhp_pharmacy',
    'bhp_variables',
    'bhp_research_protocol',
    'lab_common', 
    'lab_flag',
    'lab_grading',
    'lab_reference',
    'lab_requisition',
    'lab_aliquot_list',
    'lab_panel',
    'lab_test_code',
    'lab_account',
    'lab_patient',
    'lab_receive',
    'lab_aliquot',
    'lab_order',
    'lab_result',            
    'lab_result_item',            
    'lab_barcode',
    'lab_import_dmis',
    'lab_clinic_api',
    'lab_result_report',   
    'lab_packing',         
    'bhp_visit',
    'bhp_appointment',
    'bhp_entry',
    'bhp_lab_entry',    
    'bhp_list',
    'bhp_context',
    'bhp_dashboard',
    'bhp_dashboard_registered_subject',          
    'bhp_export_data',
    'bhp_model_describer',
    'bhp_subject_summary',
    'mpepu_list',
    'mpepu',
    'mpepu_reference',
    'mpepu_stats',
    'mpepu_maternal',        
    'mpepu_infant',
    'mpepu_infant_rando',    
    'mpepu_dashboard',    
    'mpepu_lab',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request':{
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SOUTH_LOGGING_FILE = os.path.join(os.path.dirname(__file__),"south.log")
SOUTH_LOGGING_ON = True
LOGIN_URL = '/mpepu/login/'
LOGIN_REDIRECT_URL = '/mpepu/'
LOGOUT_URL = '/mpepu/logout/'
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
LABDB = 'bhplab' 

AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"
# https://bitbucket.org/tyrion/django-autocomplete
AUTOCOMPLETE_MEDIA_PREFIX = '/media/autocomplete/media/'
DAJAXICE_MEDIA_PREFIX="dajaxice"
SESSION_COOKIE_AGE = 10000


if platform.system() == 'Darwin':
    LAB_IMPORT_DMIS_DATA_SOURCE = "DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=s012.bhp.org.bw;PORT=1433;UID=sa;PWD=cc3721b;DATABASE=BHPLAB"
else:
    LAB_IMPORT_DMIS_DATA_SOURCE = "DRIVER={FreeTDS};SERVER=192.168.1.141;UID=sa;PWD=cc3721b;DATABASE=BHPLAB"