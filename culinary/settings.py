"""
Django settings for culinary project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


import pymysql
pymysql.install_as_MySQLdb()
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-on3uso5!_yug6toip)n4die+l69j^q+$jjgcbx3ziyfmv1tkm@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['*']
import os

ALLOWED_HOSTS = [
    os.getenv('VERCEL_URL', '127.0.0.1'),
    '.vercel.app',  # Allow any Vercel subdomain
    'localhost',
]



# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # ✅ Correct Whitenoise setting
    'jazzmin',  #
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'culinary.urls'

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

WSGI_APPLICATION = 'culinary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wazobia_culinary',
#         'USER':'root',
#         'PASSWORD':'Official@lasop1',
#         'HOST':'127.0.0.1',
#         'PORT':3306
#     }
# }




# your_project/settings.py

# import pymysql
# pymysql.install_as_MySQLdb()  # Ensure pymysql is used as MySQLdb

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wazobia_culinary',
#         'USER': 'root',
#         'PASSWORD': 'Official@lasop1',
#         'HOST': '127.0.0.1',  # Example: '127.0.0.1' or 'your-remote-host'
#         'PORT': 3306,       # Default MySQL port
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         }
#     }
# }


# import os
import pymysql
pymysql.install_as_MySQLdb()
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file for local development

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'pgsuknzx_culinary'),  # ✅ Your actual database name
        'USER': os.getenv('DB_USER', 'pgsuknzx_mama'),  # ✅ Your MySQL username
        'PASSWORD': os.getenv('DB_PASSWORD', '@Mama051093'),  # ✅ Your MySQL password
        'HOST': '127.0.0.1',  # ✅ SSH tunnel (keep as 127.0.0.1)
        'PORT': os.getenv('DB_PORT', '3306'),  # ✅ Use 3307 (or 3308 if changed)
    }
}






# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# MEDIA_URL=''
# STATIC_URL = 'static/'
# STATICFILES_DIRS=[
#     os.path.join(BASE_DIR, 'school/static')
# ]
# STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
# MEDIA_ROOT= BASE_DIR/''

# STATIC_URL = '/static/'
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Static Files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "school/static")]  # Ensure 'school/static' exists
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Where static files will be collected
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Media Files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Ensure 'media' directory exists


