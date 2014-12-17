"""Development settings and globals."""

from .base import *

# ──┤ DEBUG CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#debug
DEBUG = True

# See: http://serk.io/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ BASE URL ├──────────────────────────────────────────────────────────────┐
BASE_URL = 'http://127.0.0.1:8000'
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ EMAIL CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
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
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ────────────────────────────────────────────────────────────────────────────┘
