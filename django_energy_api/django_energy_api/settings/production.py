from django_energy_api.settings.common import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['de-energy.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=env('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}

django_heroku.settings(locals())
