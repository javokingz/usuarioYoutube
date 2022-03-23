from . import db
from datetime import datetime





class Usuario(db.Model):
    __tablename__= 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    imagen = db.relationship('Img', backref = 'usuario', uselist=False)
    fecha_de_alta = db.Column(db.DateTime(), default=datetime.now())

    def __str__(self):
        return self.nombre


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))


class Contacto(db.Model):
    __tablename__= 'contacto'
    id = db.Column(db.Integer, primary_key=True)
    contacto_nick = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', backref=db.backref('usuario', lazy=True))

    def __str__(self):
        return self.contacto_nick


class Comentario(db.Model):
    __tablename__= 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.Text, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', backref=db.backref('usuario', lazy=True))
    
    def __str__(self):
        return self.comentario

class Subscripcion(db.Model):
    __tablename__= 'subscripcion'
    id = db.Column(db.Integer, primary_key=True)
    canal = db.Column(db.String(100), nullable = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', backref=db.backref('usuario', lazy=True))
    

    def __str__(self):
        return self.canal






    


