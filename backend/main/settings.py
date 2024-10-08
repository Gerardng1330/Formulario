import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'o4azh=5b&5_50o$fr1h8v!^1o96*)%rri9d-wjo5icb2_!ip6d'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'admin_modernize.apps.AdminModernizeConfig', #Admin panel UI package
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.formularios',
    'backend.auth_users',
    'backend.src_routes',
    'django_browser_reload',
    'widget_tweaks' #customize django form inputs
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Agregado para internacionalización
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Middlewares del proyecto
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'backend.main.urls'

# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR.parent / "templates" ],
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


WSGI_APPLICATION = 'backend.main.wsgi.application'

DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
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

#Internacionalización
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Control de archivos estáticos (CSS, imágenes, JavaScript)
#https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.parent / "static",
    BASE_DIR.parent / "node_modules" / "flowbite" / "dist"
]

STATIC_ROOT = BASE_DIR / "development-cdn" / "static" #Dónde queremos guardar los archivos



LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Custom user model

#Correo al mandar
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'backend.main.email_backend.EmailBackend'
EMAIL_HOST = 'mail.arvcloud.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SSL_VERIFICATION = False
EMAIL_HOST_USER = 'noreply@arvcloud.com'
EMAIL_HOST_PASSWORD = 'Jda108?jjadpa300' 
DEFAULT_FROM_EMAIL = 'noreply@arvcloud.com'

AUTH_USER_MODEL = "auth_users.User"

#ruta para descargar los cv

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = "/media/"
