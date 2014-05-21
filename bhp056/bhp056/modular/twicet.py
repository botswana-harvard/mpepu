from .base import *
from ._utils import mysql_db


DEBUG = True

TEMPLATE_DEBUG = DEBUG

KEY_PATH = join(SETTINGS_DIR, '..', '..', 'keys')

LOCALE_PATHS = ('locale',)

DATABASES = {
    'default': mysql_db(NAME='bhp056_live'),
    'lab_api': mysql_db(NAME='lab'),
}

INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1', )

DEBUG_TOOLBAR_CONFIG = {
    'RENDER_PANELS': True,
    'SHOW_COLLAPSED': False,
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
