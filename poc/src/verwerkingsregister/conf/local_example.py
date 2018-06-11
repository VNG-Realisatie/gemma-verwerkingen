"""
Any machine specific settings when using development settings.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
BASE_DIR = os.path.abspath(os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir))



# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ec_w%f)(6t3_-y17oo!lkh-9x@5)_jdp)(n68hvj^$rrhrjj-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add the hostnames or IP addresses that access this web application here.
ALLOWED_HOSTS = []

# Add a Google API key to show a map in the demo application.
GOOGLE_API_KEY = ''

# Services service via NLX:
NLX_OUTWAY_URL = 'http://localhost:12018'
KADASTER_SERVICE_URL = '{}/demo-organization/kadaster-brk'.format(NLX_OUTWAY_URL)

# If you want to use the Kadaster directly, just use:
# KADASTER_SERVICE_URL = 'https://brk.basisregistraties.overheid.nl'