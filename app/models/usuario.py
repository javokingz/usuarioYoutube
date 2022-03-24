from . import db
from datetime import datetime, date


class Usuario(db.Model):
    __tablename__= 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    imagen = db.relationship('Img', backref = 'usuario', uselist=False)
    comentario = db.relationship('Comentario')
    suscripcion = db.relationship('Suscripcion')
    fecha_de_alta = db.Column(db.DateTime(), default=datetime.now())


    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nickname': self.nickname,
            #'imagen': self.imagen.nombre
            

        }

    @classmethod
    def new(cls, nombre, nickname):
        return Usuario(nombre=nombre, nickname=nickname)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        
        except:
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False




    def __str__(self):
        return self.nombre


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    nombre = db.Column(db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True)

    @classmethod
    def new(cls, img, nombre, mimetype, usuario_id):
        return Img(img=img, nombre=nombre, mimetype=mimetype, usuario_id=usuario_id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        
        except:
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False


class Contacto(db.Model):
    __tablename__= 'contacto'
    id = db.Column(db.Integer, primary_key=True)
    contacto_nick = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario')

    def __str__(self):
        return self.contacto_nick


class Comentario(db.Model):
    __tablename__= 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.Text, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario')

    

    @classmethod
    def new(cls, comentario, usuario_id):
        return Comentario(comentario=comentario, usuario_id=usuario_id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        
        except:
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    
    def serialize(self):
        return {
            'id': self.id,
            'comentario': self.comentario,
            'usuario_id': self.usuario_id,
            'usuario': self.usuario.nickname
        }

    def __str__(self):
        return self.comentario

class Suscripcion(db.Model):
    __tablename__= 'suscripcion'
    id = db.Column(db.Integer, primary_key=True)
    canal = db.Column(db.String(100), nullable = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario')
    

    @classmethod
    def new(cls, canal, usuario_id):
        return Suscripcion(canal=canal, usuario_id=usuario_id)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        
        except:
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
    
    def serialize(self):
        return {
            'id': self.id,
            'canal': self.canal,
            'usuario':self.usuario.nickname,
           
        }
    

    def __str__(self):
        return self.canal






    


