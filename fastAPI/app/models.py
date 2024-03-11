from pydantic import BaseModel# definir una modelo para luego usarlo similar a las interfaces, ya con esto se genera tipado para cada uno de los campos
from typing import Optional # permite definir parametros como opcionales
from datetime import datetime 
#user model

class User (BaseModel):
    id: int
    nombre : str 
    apellido : str 
    direccion: Optional[str]# la direccion es un parametro opcional para el modelo
    telefono: int
    creacion_usuario: datetime = datetime.now()

# user model id
    
class UserID (BaseModel):
    id: int