# encoding: utf-8
from .base import *  # NOQA

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

USE_I18N = False

class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return 'notmigrations'


if 'MIGRATION_MODULES_OFF' in os.environ:
    MIGRATION_MODULES = DisableMigrations()
