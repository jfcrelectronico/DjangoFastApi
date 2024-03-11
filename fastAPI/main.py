from fastapi import FastAPI
import uvicorn
from app.routeres import usuario_router







app = FastAPI()
app.include_router(usuario_router.router)



if __name__ == "__main__":

    uvicorn.run("main:app",port= 8000,reload=True)#reload= True permite que la api se recargue de forma automatica sin necesidad de detener los servicios
    