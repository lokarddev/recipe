import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'uvop9ac6eiq+00)z(0j8w98utbr9j8wrtv98rbty924piuwehrgwg=%*xe3_45ks(6%&#sgtcv4dq)dim69a'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
