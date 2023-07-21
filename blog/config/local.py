from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_grupo13',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
