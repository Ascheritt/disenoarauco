from .base import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crud_django',
        'USER': 'gonza',
        'PASSWORD': 'gonza30',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
