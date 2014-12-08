"""Common settings and globals."""

from pathlib import Path

# ──┤ PATH CONFIGURATION ├────────────────────────────────────────────────────┐
# Absolute filesystem path to the Django project directory
DJANGO_ROOT = Path(__file__, '..').resolve()

# Absolute filesystem path to the top-level project directory
SITE_ROOT = DJANGO_ROOT.parent

# Site name
SITE_NAME = str(DJANGO_ROOT.name)
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ DEBUG CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#debug
DEBUG = False

# See: http://serk.io/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ MANAGER CONFIGURATION ├─────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#admins
ADMINS = (
    ('Matt Deacalion Stevens', 'matt@dirtymonkey.co.uk'),
)

# See: http://serk.io/ref/settings/#managers
MANAGERS = ADMINS
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ DATABASE CONFIGURATION ├────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(SITE_ROOT / 'db.sqlite3'),
    }
}
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ GENERAL CONFIGURATION ├─────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: http://serk.io/ref/settings/#language-code
LANGUAGE_CODE = 'en-gb'

# See: http://serk.io/ref/settings/#use-i18n
USE_I18N = True

# See: http://serk.io/ref/settings/#use-l10n
USE_L10N = True

# See: http://serk.io/ref/settings/#use-tz
USE_TZ = True
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ MEDIA CONFIGURATION ├───────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#media-root
MEDIA_ROOT = str(SITE_ROOT / 'media')

# See: http://serk.io/ref/settings/#media-url
MEDIA_URL = '/media/'
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ STATIC FILE CONFIGURATION ├─────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#static-root
STATIC_ROOT = str(SITE_ROOT / 'assets')

# See: http://serk.io/ref/settings/#static-url
STATIC_URL = '/static/'
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ SECRET CONFIGURATION ├──────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#secret-key
# Note: only used for development and testing
SECRET_KEY = 'glow in the dark body paint...'
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ SITE CONFIGURATION ├────────────────────────────────────────────────────┐
# See https://serk.io/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ TEMPLATE CONFIGURATION ├────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# See: http://serk.io/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    str(SITE_ROOT / 'templates'),
)
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ MIDDLEWARE CONFIGURATION ├──────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ URL and SSL CONFIGURATION ├─────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#root-urlconf
ROOT_URLCONF = 'apps.core.urls'

# Let Django know what to use to flag a connection as secure
SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ APP CONFIGURATION ├─────────────────────────────────────────────────────┐
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Apps specific for this project go here
LOCAL_APPS = (
    'apps.core',
    'django_extensions',
)

# See: http://serk.io/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# ────────────────────────────────────────────────────────────────────────────┘


# ──┤ WSGI CONFIGURATION ├────────────────────────────────────────────────────┐
# See: http://serk.io/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
# ────────────────────────────────────────────────────────────────────────────┘
