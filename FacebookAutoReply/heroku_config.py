"""
    HEROKU:

    Config vars change the way your app behaves. In addition to creating your own, some add-ons come with their own.
"""
import os
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print "BASE_DIR-->", BASE_DIR
print "PROJECT_ROOT-->", PROJECT_ROOT

#################################################
#            HEROKU CONFIGURATION              #
#################################################

DATABASES = {}
SECRET_KEY = None;
DEBUG=True

IS_HEROKU_ENV=False
try:
    #
    # PROD CONFIGURATION
    #

    SECRET_KEY = config('SECRET_KEY')

    DEBUG = config('DEBUG', default=False, cast=bool)

    # PostegreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

    IS_HEROKU_ENV=True

    #################################################
    #                EMAIL CONFIGURATION            #
    #################################################
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.
    REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.


except Exception as e:
    #
    # DEV CONFIGURATION
    #
    SECRET_KEY = 'cr8(rahmzqzdn*yc7u9bcq5$@^=y@t6(@8e_rr783(ef=8_(y9'

    DATABASE_PATH = os.path.join(BASE_DIR, 'octogram.db')
    DATABASES['default'] =  dj_database_url.config(default='sqlite:///'+DATABASE_PATH)

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'