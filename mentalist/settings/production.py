"""Production settings and globals."""

from os import environ
from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """
    Get the environment setting or return exception.
    """
    try:
        return environ[setting]
    except KeyError:
        error_msg = 'Set the {} env variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# ──┤ HOST CONFIGURATION ├────────────────────────────────────────────────────┐
# See: http://serk.io/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*', ]
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ BASE URL ├──────────────────────────────────────────────────────────────┐
BASE_URL = 'http://berg.dirtymonkey.co.uk'
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ EMAIL CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: http://serk.io/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: http://serk.io/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', 'your-password')

# See: http://serk.io/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your-email')

# See: http://serk.io/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: http://serk.io/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[{}] '.format(SITE_NAME)

# See: http://serk.io/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: http://serk.io/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ DATABASE CONFIGURATION ├────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mentalist',
        'USER': 'mentalist',
        'PASSWORD': 'mentalist',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ CACHE CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ SECRET CONFIGURATION ├──────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
# ────────────────────────────────────────────────────────────────────────────┘
