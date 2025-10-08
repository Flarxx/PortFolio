from pathlib import Path
import os

# =========================================
# === RUTAS BASE ===
# =========================================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================
# === CONFIGURACIÓN GENERAL ===
# =========================================
SECRET_KEY = 'django-insecure-h@_-*+!t891%7$l3686_yqn_aicd^pf)5-%+yn_r7b)aewwn7_'
DEBUG = True
ALLOWED_HOSTS = []


# =========================================
# === APLICACIONES INSTALADAS ===
# =========================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nucleo',  # Tu aplicación principal
]


# =========================================
# === MIDDLEWARE ===
# =========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================================
# === CONFIGURACIÓN DE URLS Y WSGI ===
# =========================================
ROOT_URLCONF = 'PortFolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 permite usar tu carpeta templates global
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

WSGI_APPLICATION = 'PortFolio.wsgi.application'


# =========================================
# === BASE DE DATOS ===
# =========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================================
# === VALIDACIÓN DE CONTRASEÑAS ===
# =========================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================================
# === CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA ===
# =========================================
LANGUAGE_CODE = 'es-ve'  # Cambiado a español (Venezuela)
TIME_ZONE = 'America/Caracas'
USE_I18N = True
USE_TZ = True


# =========================================
# === ARCHIVOS ESTÁTICOS Y MULTIMEDIA ===
# =========================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# 🖼 Archivos subidos (como tus certificados)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================================
# === CONFIGURACIÓN ADICIONAL ===
# =========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
