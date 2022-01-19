from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
DATABASE_ROUTERS = [
    'votes.routers.MultiDBRouter'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    },
    'vote_db1' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME2'),
        'USER': env('DATABASE_USER2'),
        'PASSWORD': env('DATABASE_PASSWORD2'),
        'HOST': env('DATABASE_HOST2'),
        'PORT': env('DATABASE_PORT2'),
    }
}
