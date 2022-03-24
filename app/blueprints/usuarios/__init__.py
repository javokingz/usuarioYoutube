from flask import  Blueprint, request, jsonify
from flask import request
from app.responses import response 
from app.responses import not_found
from app.responses import bad_request
from werkzeug.utils import secure_filename

from app.models.usuario import *


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/usuarios', methods=['GET'])
def get_usuarios():
    
    usuarios = Usuario.query.all()
    return response([
        usuario.serialize() for usuario in usuarios
    ])
    

@api.route('/usuario/<id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    
    if usuario is None:
        return not_found()
    
    return response(usuario.serialize())


@api.route('/usuarios', methods=['POST'])
def create_usuario():
    json = request.get_json(force=True)
    
    if json.get('nombre') is None:
        return bad_request()

    if json.get('nickname') is None:
        return bad_request()
    
    usuario = Usuario.new(json['nombre'], json['nickname'])
    if usuario.save():

        return response(usuario.serialize())
    
    return bad_request()


@api.route('/usuario/<id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    
    if usuario is None:
        return not_found()
    
    
    json = request.get_json(force=True)

    usuario.id = json.get('id', usuario.id)
    usuario.nombre = json.get('nombre', usuario.nombre)
    usuario.nickname = json.get('nickname', usuario.nickname)

    if usuario.save():
        return response(usuario.serialize())
    
    return bad_request()

@api.route('/usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()

    if usuario is None:
        return not_found()
    
    if usuario.delete():
        return {'message': 'Se elimino con exito'}
    return bad_request()


#View para subir imagenes para usuarios

@api.route('/upload_imagen', methods=['POST'])
def upload_imagen():
    pic = request.files['pic']
    usuario_id = request.form['usuario_id']
    if not pic:
        return bad_request()

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return bad_request()


    img = Img(img=pic.read(), nombre=filename, mimetype=mimetype,  usuario_id=usuario_id)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


#Endpoints para comentarios


@api.route('/comentarios', methods=['POST'])
def create_comentario():
    json = request.get_json(force=True)
    
    if json.get('comentario') is None:
        return bad_request()

    if json.get('usuario_id') is None:
        return bad_request()
    
    comentario = Comentario.new(json['comentario'], json['usuario_id'])
    if comentario.save():

        return response(comentario.serialize())
    
    return bad_request()

@api.route('/comentarios', methods=['GET'])
def get_comentarios():
    
    comentarios = Comentario.query.all()
    return response([
        comentario.serialize() for comentario in comentarios
    ])


#Endpoints para suscripciones


@api.route('/suscripciones', methods=['POST'])
def create_suscripcion():
    json = request.get_json(force=True)
    
    if json.get('canal') is None:
        return bad_request()

    if json.get('usuario_id') is None:
        return bad_request()
    
    suscripcion = Suscripcion.new(json['canal'], json['usuario_id'])
    if suscripcion.save():

        return response(suscripcion.serialize())
    
    return bad_request()

@api.route('/suscripciones', methods=['GET'])
def get_suscripcion():
    
    suscripciones = Suscripcion.query.all()
    return response([
        suscripcion.serialize() for suscripcion in suscripciones
    ])