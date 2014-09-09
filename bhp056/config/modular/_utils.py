from os import environ

from django.core.exceptions import ImproperlyConfigured


class DBConfig(object):
    def __init__(self, dbconfig, **kwargs):
        self.dbconfig = dbconfig.copy()
        self.dbconfig.update(kwargs)

    def __call__(self, **kwargs):
        result = self.dbconfig.copy()
        result.update(kwargs)
        return result


_mysql_base_config = {
    'ENGINE': 'django.db.backends.mysql',
    'OPTIONS': {
        'init_command': 'SET storage_engine=INNODB'
    },
    'USER': 'root',
    'HOST': '',
    'PORT': '3306',
}

_sqlite_base_config = {
    'ENGINE': 'django.db.backends.sqlite3',
    'USER': 'root',
    'PASSWORD': 'cc3721b',
    'HOST': '',
    'PORT': ''
}

mysql_db = DBConfig(_mysql_base_config, PASSWORD='cc3721b')

sqlite_db = DBConfig(_sqlite_base_config, PASSWORD='cc3721b')


def env(var_name):
    """get an environment variable"""
    try:
        return environ[var_name]
    except:
        raise ImproperlyConfigured("Set the %s environment variable" % var_name)


def customize(base_dict, **kwargs):
    """Immutable dictionary updater or merger."""
    result = base_dict.copy()
    result.update(kwargs)
    return result
