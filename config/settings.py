"""
Configuration du projet Django Gestion RH
"""

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète (depuis variable d'environnement)
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

# Mode debug (False en production)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hôtes autorisés
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Whitenoise pour les fichiers statiques
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

# Configuration des URLs racines
ROOT_URLCONF = 'config.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'rh' / 'templates'],
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

# Configuration WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rh',  # Notre application unique
]

# Base de données - PostgreSQL via DATABASE_URL (Render) ou locale
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', 'postgres://postgres:nito2005@127.0.0.1:5432/gestionRH'))
}

# Validation des mots de passe
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

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'rh' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Fichiers médias
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Type de clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URLs de connexion/déconnexion
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
