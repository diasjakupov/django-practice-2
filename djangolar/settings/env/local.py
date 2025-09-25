from settings.base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='django-insecure-t)ky91z4_8se5tk^x9xqgxthaetxiz^)$6&#$iski2p5##b4_z')

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}