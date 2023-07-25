from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grupo13',
        'USER' : 'root',
        'PASSWORD' : '<contraseña_mysql>',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
