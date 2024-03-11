# pasos para crear fastapi
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

4) crear archivo de librerias necesarias (requirements.txt) con contenido
fastapi
uvicorn

5) ejecuatar este archivo
pip install -t ./requirements.txt

6) crear archivo main.py

from fastapi import FastAPI

app= FastAPI()

7) para correr archivo creado usar

uvicorn main: app (nombre del archivo creado : instancia de FastApi)

o agreganado las lineas

    if __name__ == "__main__":
        uvicorn.run("main:app",port= 8000)
    
    y luego correr 

    python ./main.py

8) ver en el browser la documentacion

localhost:8000/docs






