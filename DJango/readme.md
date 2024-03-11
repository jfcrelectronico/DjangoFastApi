# crear proyecto en django
1) instalar virtualenv

pip install virtualenv

o

python -m venv venv

2) crear la carpeta donde se desarrollara en ambiente virtual

virtualenv venv(nombre puede cambiar segun se desee)

3) habilitar ambiente virtual
para linux
source venv/bin/activate
para windows
.\venv\Scripts\activate.ps1

4) instalar django

python -m pip install django

5) iniciar proyecto django

django-admin startproject sap

6) moverse a la carpeta del projecto django creado

7) ejecutar el archivo manage.py

python manage.py runserver

8) cada parte de la aplicacion se base en pequñas app,para crear una app

estando dentro del projecto ejectuar

python manage.py startapp nombreappdeseado

9) cada vez que se cree una app se debe registrar, dentro del los archivos del proyecto buscar settings
y dentro de la lista de aplicaciones instaladas INSTALLED_APP se agrega al final de la lista el nombre de la app

'nombreappdeseada',

10) dentro del archivo de urls.py estan los diferentes paths, agregar dentro de urlpatterns el los diferentes paths deseados

path('nombrepathdeseado/',nombre_funcion_a_llamar)


la funcion_a_llamar debe hacer parte de las funciones dentro del archivo views.py de la app creada

11) en el archivo views.py respectivo crear la funcion

def nombre_funcion_a_llamar(request):
    return HttpResponse('Mensaje deseado')# importar HttpResponse
12) dentro del archivo urls.py agregar importar la ruta donde se aloja la funcion que llamara el path agregado en el paso 10

13) para conectar la aplicacion a una base de datos, se debe configurar el campo DATABASE dentro del archivo settings.py

14) instalar libreria para conexion a base de datos en python psycopg2

pip install psycopg2-binary

14) instalar mongo

python -m pip install "pymongo[srv]"




