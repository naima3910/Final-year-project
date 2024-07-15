import os
import posixpath
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')


DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

ALLOWED_HOSTS = ['medisom.site','www.medisome.site','127.0.0.1', 'localhost']


INSTALLED_APPS = [
    'login',
    'dashboard',
    'patientmeds',
    'patientcontact',
    'patientmedicalhistory',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'defender',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'defender.middleware.FailedLoginMiddleware',
]

DEFENDER_REDIS_URL = os.getenv('DEFENDER_REDIS_URL')
DEFENDER_LOGIN_FAILURE_LIMIT = 3  # Number of failed login attempts before locking out
DEFENDER_COOLOFF_TIME = 300  # Time (in seconds) to lock out after failure limit is reached

ROOT_URLCONF = 'EMR.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'EMR.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'EMR',
        'CLIENT': {
            'host': os.getenv('MONGO_HOST'),
            'username': os.getenv('MONGO_USERNAME'),
            'password': os.getenv('MONGO_PASSWORD'),
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators


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

AUTH_USER_MODEL = 'login.PatientLogin'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# CSRF settings
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True

CSRF_TRUSTED_ORIGINS = [
    'https://medisom.site',
    'https://www.medisom.site',
    'http://127.0.0.1',
    'http://localhost'
]


# Session settings
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True

# Login URLs
LOGIN_REDIRECT_URL = '/dashboard/' 
LOGIN_URL = '/login/'  
# Internationalisation

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
