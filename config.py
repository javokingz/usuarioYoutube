class Config:
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/usuarios.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    
config = {
        'development': DevelopmentConfig
}