import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uvop9ac6eiq+00)z(wg=%*xe3_45ks(6%&#sgtcv4dq)dim69a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recipe',
        'USER': 'postgres',
        'PASSWORD': 'lok1415161213',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
