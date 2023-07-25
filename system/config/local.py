from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blognuevo1',
        'USER' : 'root',
        'PASSWORD' : 'root',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
