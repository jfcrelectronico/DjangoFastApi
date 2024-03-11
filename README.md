# Creacion de FastApi basica con conexion a Mongo DB
1) instalar virtualenv
    *pip install virtualenv
    o
    *python -m venv venv

2) crear la carpeta donde se desarrollara en ambiente virtual
    virtualenv venv(nombre puede cambiar segun se desee)

3) habilitar ambiente virtual:
    para linux source venv/bin/activate 
    para windows .\venv\Scripts\activate.ps1

4) crear archivo de librerias necesarias (requirements.txt) con contenido fastapi uvicorn pymongo

5) ejecuatar este archivo pip install -t ./requirements.txt (antes de ejecutar ubiquese en la ruta donde esta el ambiente virtual que lanzo)

6) crear archivo main.py
    from fastapi import FastAPI
    import uvicorn

    from fastapi import FastAPI
    app= FastAPI()

    *para correr archivo creado usar
    uvicorn main: app (nombre del archivo creado : instancia de FastApi)

    o agreganado las lineas

    if __name__ == "__main__":
        uvicorn.run("main:app",port= 8000)

    y luego correr 

    *python ./main.py
    ver en el browser la documentacion
    localhost:8000/docs
7) crear folder config donde se almacenara la configuracion de conexion a la base de datos para este caso MONGO atravez de pymongo

8) crear folder models donde se describira la estructura de la base de datos

9) crear folder schema donde se describen las funciones que permiten la depuracion de los datos a enviar o traer de la base de datos,al ser mongo Listas y diccionarios
