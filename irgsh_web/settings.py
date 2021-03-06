import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
# Django settings for web_builder project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': 'irgsh.db',
    }
}

DEFAULT_FROM_EMAIL = 'webmaster@blankon.in'
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.welho.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '25'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Jakarta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = unicode(os.path.join(PROJECT_PATH, 'media')) 

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i6$x6c38p5#8a^qj6_j^@3@32pz!7k$ed2s+qebqa^yp=xxc1o'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS = (
     os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_openid_auth',
    'south',
    'irgsh_web',
    'irgsh_web.account',
    'irgsh_web.repo',
    'irgsh_web.build',
    'irgsh_web.package',
    'djcelery',
    'debug_toolbar',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: '/user/%s/' % o.username
}

INTERNAL_IPS = ('127.0.0.1', '192.168.56.1',)

OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/'
OPENID_SSO_SERVER_URL = "http://82.181.46.34:8081/o/"
FULL_LOGOUT_URL = "http://82.181.46.34:8081/logout"
OPENID_USE_AS_ADMIN_LOGIN = True

LOG_PATH = 'run/logs'


ROOT_URLCONF = 'irgsh_web.urls'

import djcelery
djcelery.setup_loader()

CELERY_QUEUES = {
    'celery': {
        'exchange': 'celery',
        'exchange_type': 'direct',
    },
}
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_DEFAULT_EXCHANGE = 'celery'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

BROKER_HOST = 'irgsh.dahsy.at'
BROKER_PORT = 5672
BROKER_USER = 'irgsh'
BROKER_PASSWORD = 'irgsh'
BROKER_VHOST = 'irgsh'

# Certificate for task init worker
SSL_KEY = 'taskinit-ssl.key'
SSL_CERT = 'taskinit-ssl.pem'

SOURCE_UPLOAD_PATH = 'incoming/'
SOURCE_UPLOAD_HOST = 'upload.irgsh.dahsy.at'
SOURCE_UPLOAD_USER = 'upload'
SOURCE_UPLOAD_PORT = 2222
SOURCE_UPLOAD_KEY = 'taskinit-ssh.key'

DOWNLOAD_TARGET = 'static/source/'

SERVER = 'https://irgsh.dahsy.at:9443/'
REPO_UPLOAD_SERVE = 'irgsh-upload-serve'

TWITTER_CONFIG = dict(CONSUMER_KEY=None,
                      CONSUMER_SECRET=None,
                      ACCESS_TOKEN_KEY=None,
                      ACCESS_TOKEN_SECRET=None)
SHORT_URL = 'http://p.blankon.in/'

AUTH_PROFILE_MODULE = 'account.UserProfile'

LOCAL_SETTINGS = os.path.join(PROJECT_PATH, 'localsettings.py')
if os.path.exists(LOCAL_SETTINGS):
    execfile(LOCAL_SETTINGS)

EXTRA_SETTINGS = '/etc/irgsh/web/settings.py'
if EXTRA_SETTINGS is not None and os.path.exists(EXTRA_SETTINGS):
    execfile(EXTRA_SETTINGS)

EXTRA_SETTINGS_DIR = '/etc/irgsh/web/settings.py.d'
if EXTRA_SETTINGS_DIR is not None:
    from glob import glob
    mods = sorted(glob(os.path.join(EXTRA_SETTINGS_DIR, '*.py')))
    for mod in mods:
        execfile(mod)

