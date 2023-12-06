"""
Django settings for global_computer project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.getenv('DEBUG', False) == 'False'


### ------ DJANGO APP SECURITY -------###
# Cross-site Scripting for deploy
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# # SSL redirect
# SECURE_SSL_REDIRECT = True

# # HTTP Strict Transport Security
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# #  Cross-site request forgery (CSRF) protection
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

## ------ END DJANGO APP SECURITY -------##



ALLOWED_HOSTS = ['127.0.0.1','localhost', '134.209.97.214']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'global_computer_api',
    'account',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_cleanup.apps.CleanupConfig',
    'phonenumber_field',
    # 'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'global_computer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'global_computer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


### ------ MUST COMMENT IN LOCAL DATABASE BEFORE FINAL PUSH ------ ###






### ------ MUST COMMENT OUT GLOBAL DATABASE BEFORE FINAL PUSH ------ ###

# if os.getenv('DEBUG', False) == 'False':
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        # 'OPTIONS': {'sslmode': 'require'},
    }
}

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': 'glc_db',
    #         'USER': 'jahidul',
    #         'PASSWORD': 'J@hidul42598475',
    #         'HOST': 'localhost',
    #         'PORT': '3306',
    #         # 'OPTIONS': {'sslmode': 'require'},
    #     }
    # }
    

# else:

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }






# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'account.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
MEDIA_URL = "/media/"


# STATIC_DIRS = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_DIRS = '/home/jahidul/global_computer_api/static'
STATIC_ROOT = '/home/jahidul/global_computer_api/static'

MEDIA_ROOT = '/home/jahidul/global_computer_api/media'



CORS_ALLOW_ALL_ORIGINS = True





# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
}



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}








DJOSER  = {
    'USER_ID_FIELD': 'username',
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
}