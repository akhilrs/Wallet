import os
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_mongodb_engine',
#         'NAME': os.environ.get('MASTER_DB'),
#         'USER': os.environ.get('MASTER_DB_USER'),
#         'PASSWORD': os.environ.get('MASTER_DB_PASSWORD'),
#         'HOST': os.environ.get('MASTER_DB_HOST'),
#         'PORT': os.environ.get('MASTER_DB_PORT')
#     }

# mongodb connection
from mongoengine import connect
connect('wallet')

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


