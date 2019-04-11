# encoding: utf-8
from .base import *  # NOQA

# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# TOOLBAR CONFIGURATION
INSTALLED_APPS += ('debug_toolbar',)

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
