# PROYECTO FINAL INFORMATORIO COHORTE 2023
## TEMATICA: BLOG
### GRUPO: 13
### MENTOR DESIGNADO: .....


INTEGRANTES: 
   - ZENIQUEL, Camila
   - ROLON, Dario
   - RAMIREZ, Claudio
   - MIRANDA, Federico
   - HIEBL, Darian   

   - GOMEZ, Jonatan   
   - VAERNET, Bianca
   - LOPEZ, Andres

**Comandos utiles:**

* instalar dependencias:
con el entorno virtual activado y en la ruta de proyecto 
pip install -r requirements.txt

* servir aplicacion: 
en ruta de proyecto
py manage.py runserver

* agregar aplicaciones: 
en ruta apps\ - django-admin startapp <nombre de aplicacion> 

* configurar local.py 
En archivo local.py ubicado en blog/config/ colocar los datos de la base de datos local 
de cada uno. local.py  

por ejemplo:  

<local.py> 
'from .settings import *  

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'blog_grupo13', 
        'USER' : 'root', 
        'PASSWORD' : 'root', 
        'HOST' : 'localhost', 
        'PORT' : '3306', 
    } 
} '

