"""
Django settings for fi_django_project project.
PROD environment
"""

from .common import *

from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['194.58.111.25']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# !!!!!!! TO BE CHANGED to Postgres !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# EXTENDED SETTINGS
# ==============================

# !!!!!!! TO BE CHANGED to one host only !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CORS_ALLOW_ALL_ORIGINS = True
