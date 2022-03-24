
# Prueba para Waco
## Javier Reyes Rodríguez
------
## Instalación

Para realizar la instalación de es necesario correr el comando:

```
pip install  -r requirements.txt
```
Nota: es recomendable generar un ambiente virual para dicha instalación.

Una vez quede instalado los requerimientos, ubicarse en la raiz del proyecto y correr el comando:
 
```
python main.py
```

Ya que el servidor se aya levantado, en tu navegardo coloca la url 
http://127.0.0.1:5000/

------
## Endpoints
 A continuacion se muestran los endpoints para realizar pruebas con la API.

 ### Usuario:

GET:
http://127.0.0.1:5000/api/usuarios


POST:
http://127.0.0.1:5000/api/usuarios

Ejemplo: 
```json
{
    "nombre": "Javier Reyes",
     "nickname": "javireyes"
}
```
GET: http://127.0.0.1:5000/api/usuario/{id}

PUT: http://127.0.0.1:5000/api/usuario/{id}

DELETE: http://127.0.0.1:5000/api/usuario/{id}


### Comentario:

GET: http://127.0.0.1:5000/api/comentarios

POST: http://127.0.0.1:5000/api/comentarios

Ejemplo: 
```json
{
    "comentario": "Este es un comentario de prueba...",
     "usuario_id":  1
}
```

### Suscripcion:


GET: http://127.0.0.1:5000/api/suscripciones

POST: http://127.0.0.1:5000/api/suscripciones

Ejemplo: 
```json
{
    "canal": "LevelUp",
     "usuario_id":  1
}
```

### Imagenes:

Para ingresar imagenes  se requiere usar el archivo index.html ubicado en la raíz del proyecto, en el formulario es posible hacer el upload del archivo así como colocar el id del usuario al cual se asignara dicha imagen.
