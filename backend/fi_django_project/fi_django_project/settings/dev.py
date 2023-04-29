"""
Django settings for fi_django_project project.
DEV environment
"""

print("============== DEV MODULE FOUND ===================")

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# EXTENDED SETTINGS
# ==============================

CORS_ALLOW_ALL_ORIGINS = True
