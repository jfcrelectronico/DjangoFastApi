from fastapi import APIRouter
from app.models import User,UserID

usuarios =[]

router = APIRouter(

    prefix= '/usuario',
    tags=['Users']
)

@router.post('/crear_usuario')

def crear_usuario(user:User): #se recibe un usuario pero este debe ser del tipo User definido en la clase User que heredo de la clase BaseModel 
    #print(user.model_dump())# dict esta en desuso para BaseMOdel en vez de ello se usa model_dump
    usuarios.append(user.model_dump())
    ##for items in usuarios :
        ##return{items}
    #return {"usuario_registrado_telefono": user.telefono} 
    return {"Respuesta ": "Se creo usuario de forma satisfactoria" }

@router.get('/{user_id}')# se envia un query parameter a travez de la url
def obtener_usuario(user_id: int):#trae todos los usuarios de la lista actual
    for items in usuarios:
        if items["id"] == user_id:
            return {f"Usuario {user_id}" : items}
    return {f"Usuario con id {user_id}" : "No encontrado en la lista"}

@router.post('/')
def obtener_usuario2(user_id:UserID):#se envia la peticion a travez del body sin el usuo de queryparameters
    for items in usuarios:
        if items["id"] == user_id.id:
            return {f"Usuario {user_id.id}" : items}
    return {f"Usuario con id {user_id.id}" : "No encontrado en la lista"}

@router.get('/')
def obtener_usuarios():#trae todos los usuarios de la lista actual
    return usuarios

@router.delete('/{user_id}')#recibe un id por query parameter para eleminar un usuario por su id
def borrar_usuario(user_id:int):
    for index,user in enumerate(usuarios):# generar el index o posicion dentro del arreglo y el contenido de la posicion
        #print(index,user)
        if user["id"]== user_id:# comparar el id reibido por query parameter con la llave del contenido actual explodaro dentro del arreglo
            usuarios.pop(index)# borrar el contenido en la posicion indicada
            return {f"Usuario con id {user_id}": "fue elemininado con exito"}
    return {f"Usuario con id {user_id}" : "No encontrado en la lista"}


@router.put('/{user_id}')
def actualizar_usuario(user_id:int, updateUser: User):
    for index,user in enumerate(usuarios):# generar el index o posicion dentro del arreglo y el contenido de la posicion
        #print(index,user)
        if user["id"]== user_id:# comparar el id reibido por query parameter con la llave del contenido actual explodaro dentro del arreglo
            usuarios[index]["id"] = updateUser.model_dump()["id"]
            usuarios[index]["nombre"] = updateUser.model_dump()["nombre"]
            usuarios[index]["apellido"] = updateUser.model_dump()["apellido"]
            usuarios[index]["direccion"] = updateUser.model_dump()["direccion"]
            usuarios[index]["relefono"] = updateUser.model_dump()["telefono"]
            return {f"el usuario con id {user_id}": "fue actualizado"}
    return {f"Usuario con id {user_id}" : "No pudo ser actualiado"}