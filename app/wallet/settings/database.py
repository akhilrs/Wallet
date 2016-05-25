import os
from django_replicated.settings import *
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# DATABASE_ROUTERS = ['wallet.core.replica_router.DefaultReplicaRouter']
DATABASE_ROUTERS = ['wallet.chat.db_router.ChatDBRouter']
REPLICATED_DATABASE_SLAVES = ['replica1', 'replica2']
REPLICATED_DATABASE_DOWNTIME = 20
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('MASTER_DB'),
        'USER': os.environ.get('MASTER_DB_USER'),
        'PASSWORD': os.environ.get('MASTER_DB_PASSWORD'),
        'HOST': os.environ.get('MASTER_DB_HOST'),
        'PORT': os.environ.get('MASTER_DB_PORT')
    },
    'replica1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('REPLICA1_DB'),
        'USER': os.environ.get('REPLICA1_DB_USER'),
        'PASSWORD': os.environ.get('REPLICA1_DB_PASSWORD'),
        'HOST': os.environ.get('REPLICA1_DB_HOST'),
        'PORT': os.environ.get('REPLICA1_DB_PORT')
    },
    'replica2': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('REPLICA2_DB'),
        'USER': os.environ.get('REPLICA2_DB_USER'),
        'PASSWORD': os.environ.get('REPLICA2_DB_PASSWORD'),
        'HOST': os.environ.get('REPLICA2_DB_HOST'),
        'PORT': os.environ.get('REPLICA2_DB_PORT')
    },
    'chat_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('CHAT_DB'),
        'USER': os.environ.get('CHAT_DB_USER'),
        'PASSWORD': os.environ.get('CHAT_DB_PASSWORD'),
        'HOST': os.environ.get('CHAT_DB_HOST'),
        'PORT': os.environ.get('CHAT_DB_PORT')
    },
}

# mongodb connection
MONGODB_DATABASES = {
    "default": {
        "name": os.environ.get('MASTER_DB'),
        "host": os.environ.get('MASTER_DB_HOST'),
        "password": os.environ.get('MASTER_DB_PASSWORD'),
        "username": os.environ.get('MASTER_DB_USER'),
        "tz_aware": True,  # if you using timezones in django (USE_TZ = True)
    },
}
# }
