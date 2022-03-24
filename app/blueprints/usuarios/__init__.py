from flask import  Blueprint, request, jsonify
from flask import request
from app.responses import response 
from app.responses import not_found
from app.responses import bad_request

from app.models.usuario import *


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/hello_world')
def hello_world():
    return {'message': 'Hello World!'}


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


@api.route('/dispositivo/<id>', methods=['PUT'])
def update_dispositivo():
    pass

@api.route('/dispositivo/<id>', methods=['DELETE'])
def _dispositivo():
    pass
