from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'recipe_app',
    'django_summernote',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'graphene_django',
    'django_filters',
]

MIDDLEWARE = [
    'recipe_app.middleware.StackOverflow',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recipe_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'recipe_app.context_processors.add_variable'
            ],
        },
    },
]

WSGI_APPLICATION = 'recipe_config.wsgi.application'


# this parameter is just for testing, in prod environment you should better use per_view cache
CACHE_MIDDLEWARE_SECONDS = 1


SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# graphql root schema path
GRAPHENE = {
    "SCHEMA": "recipe_app.api.schema.schema"
}


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


# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# static directory settings
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# media directory settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# flatpage settings
SITE_ID = 3


# auth settings
LOGIN_REDIRECT_URL = 'user_profile'
LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_EMAIL_VERIFICATION = 'none'


# email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# clickjacking protection allows to show Summernote editor frame correctly
X_FRAME_OPTIONS = 'SAMEORIGIN'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# to divide different settings files
try:
    from .local_settings import *
except ImportError:
    # from .prod_settings import *
    pass
