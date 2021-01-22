from django_energy_api.settings.common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'energy',
        'TEST': {
            'NAME': 't_energy'
        },
        'USER': 'def',
        'PASSWORD': env('PASSWORD'),
        'HOST': 'localhost',
        'DISABLE_SERVER_SIDE_CURSORS': True
    }
}
