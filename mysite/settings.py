"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
from decouple import config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6x$tjy^k$7lb5utvb6&3w+2kj#f3m#_d8g*l9mfr%2@r39&pfa'

# SECURITY WARNING: don't run with debug turned on in produexction!
# DEBUG = False  --> in server 
DEBUG = True  # in localhost 

#ALLOWED_HOSTS = ['hightech-metrology.com', 'www.hightech-metrology.com']  # in server , now the first one will not be in server.
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']  # in local 

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en', _('English')), 
    ('de', _('German')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('pl', _('Polish')),
    ('it', _('Italian')),
    ('tr', _('Turkish')),
    ('ru', _('Russian')),

]


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),    
    os.path.join(BASE_DIR, 'about_page', 'locale'),   
    os.path.join(BASE_DIR, 'accessories', 'locale'),   
    os.path.join(BASE_DIR, 'callibrators', 'locale'),  
    os.path.join(BASE_DIR, 'contact_page', 'locale'), 
    os.path.join(BASE_DIR, 'dimensional_measurement', 'locale'),
    os.path.join(BASE_DIR, 'leak_testing', 'locale'),
    os.path.join(BASE_DIR, 'products_page', 'locale'),
    os.path.join(BASE_DIR, 'services', 'locale'),
    
    ]




# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'about_page.apps.AboutPageConfig',
    'contact_page.apps.ContactConfig',
    'products_page.apps.ProductsPageConfig', 
    'dimensional_measurement.apps.DimensionalMeasurementConfig',
    'leak_testing.apps.LeakTestingConfig',
    'callibrators.apps.CallibratorsConfig',
    'services.apps.ServicesConfig',
    'accessories.apps.AccessoriesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',
    'rosetta', #NEW
    'imagekit', 
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'mysite.middleware.RedirectToWWWMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"], #new
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True








# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = '/static/'


STATIC_URL = '/static/' # to run in server 1 


#STATIC_ROOT = '/home/highpkui/public_html/static' # to run in server 2 


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#EMAIL_HOST =  'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT =  587
#EMAIL_HOST_USER =  'karaaliogluseyit@gmail.com'
#EMAIL_HOST_PASSWORD =  'dcxxnbjtzbosptbx'


EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'



EMAIL_HOST =  'mail.kaometrology.com'
EMAIL_USE_TLS = True
EMAIL_PORT =  465
EMAIL_HOST_USER =  'kaan.karaalioglu@kaometrology.com'
EMAIL_HOST_PASSWORD =  config('EMAIL_HOST_PASSWORD')


RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')



