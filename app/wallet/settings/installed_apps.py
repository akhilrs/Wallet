# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'mongonaut',
    'channels',
    'django_mongoengine',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
)

LOCAL_APPS = (
    'wallet.chat',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
INSTALLED_APPS = sorted(list(set(INSTALLED_APPS)))