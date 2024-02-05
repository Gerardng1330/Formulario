import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'o4azh=5b&5_50o$fr1h8v!^1o96*)%rri9d-wjo5icb2_!ip6d'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Aplicaciones del proyecto
    'formularios',
    'login',
    'password',
    'registro',
        #frontend
        'django_browser_reload'
     
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd" #path de node.js en tu computadora. cmd -> where npm. prueba entre \ y /

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Middlewares del proyecto
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'main.urls'

# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'formularios/templates')],
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


WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'manudb',
           'USER': 'manuel',
           'PASSWORD': '123',
           'HOST': '200.46.88.101',
           'PORT': '5432',
       }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Control de archivos estáticos (CSS, imágenes, JavaScript)
#https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "development-cdn" / "static" #Dónde queremos guardar los archivos

#Internacionalización
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Custom user model

#Correo al mandar
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'password.backends.email_backend.EmailBackend'
EMAIL_HOST = 'mail.arvcloud.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SSL_VERIFICATION = False
EMAIL_HOST_USER = 'noreply@arvcloud.com'
EMAIL_HOST_PASSWORD = 'Jda108?jjadpa300' 

AUTH_USER_MODEL = "registro.User"