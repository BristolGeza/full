import os
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-deployment-domain.com', '127.0.0.1']

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR) / 'staticfiles'

# Add CSRF trusted origins for the production domain
CSRF_TRUSTED_ORIGINS = ['https://your-deployment-domain.com']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Other middleware...
]

