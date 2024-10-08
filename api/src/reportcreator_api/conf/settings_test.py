from reportcreator_api.conf.settings import *  # noqa: F403
from reportcreator_api.conf.settings import INSTALLED_APPS, REST_FRAMEWORK, STORAGES

STORAGES = STORAGES | {
    'uploaded_images': {'BACKEND': 'django.core.files.storage.InMemoryStorage'},
    'uploaded_assets': {'BACKEND': 'django.core.files.storage.InMemoryStorage'},
    'uploaded_files': {'BACKEND': 'django.core.files.storage.InMemoryStorage'},
    'archived_files': {'BACKEND': 'django.core.files.storage.InMemoryStorage'},
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

REST_FRAMEWORK |= {
    'DEFAULT_THROTTLE_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']
MFA_FIDO2_RP_ID=''


LOCAL_USER_AUTH_ENABLED = True
REMOTE_USER_AUTH_ENABLED = True
REMOTE_USER_AUTH_HEADER = 'Remote-User'
AUTHLIB_OAUTH_CLIENTS = {}


ELASTIC_APM_ENABLED = False
ELASTIC_APM_RUM_ENABLED = False
CELERY_TASK_ALWAYS_EAGER = True
NOTIFICATION_IMPORT_URL = None


ENABLE_PRIVATE_DESIGNS = True
DISABLE_SHARING = False
SHARING_PASSWORD_REQUIRED = False
SHARING_READONLY_REQUIRED = False
ARCHIVING_THRESHOLD = 1
AUTOMATICALLY_ARCHIVE_PROJECTS_AFTER = None
AUTO_DELETE_ARCHIVE_AFTER = None

PREFERRED_LANGUAGES = ['en-US', 'de-DE']

INSTALLATION_ID = 'dummy-installation-id-used-in-unit-test'
BACKUP_KEY = 'dummy-backup-key-used-in-unit-test'


# Disable plugins
ENABLED_PLUGINS = []
INSTALLED_APPS = [app for app in INSTALLED_APPS if not app.startswith('sysreptor_plugins.')]


# Disable license check
from reportcreator_api.utils import license  # noqa: E402

license.check_license = lambda **kwargs: {'type': license.LicenseType.PROFESSIONAL, 'users': 1000, 'name': 'Company Name'}
