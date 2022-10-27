from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db

# class Pessoa(db.Model):
  
#     id = db.Column(db.Integer(), primary_key = True)
#     nome = db.Column(db.String(80))
#     whatsapp = db.Column(db.Integer())
#     endereco = db.Column(db.String())
#     email = db.Column(db.String())
#     # hash_pwd = db.Column(db.String(100))
   

#     def __init__(self , nome, whatsapp, endereco, email, hash_pwd = ''):
#         self.nome = nome
#         self.whatsapp = whatsapp
#         self.endereco = endereco
#         self.email = email
#         self.hash_pwd = hash_pwd
    
#     @classmethod
#     def find_by_id(cls, id):
#         return cls.query.filter_by(id = id).first()
    
#     @classmethod
#     def search_all(cls):
#         return cls.query.all()
    
#     def toDict(self):
#         return {"nome": self.nome, "whatsapp": self.whatsapp, "endereco": self.endereco, "email": self.email, "hash_pwd": self.hash_pwd}



class EmpreendedorModel(db.Model):
    __tablename__ = 'empreendedor'
    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(80))
    whatsapp = db.Column(db.String())
    endereco = db.Column(db.String())
    email = db.Column(db.String())

    cnpj= db.Column(db.String(100))
    perfil= db.Column(db.String(100))
 
    def __init__(self, nome ,whatsapp, endereco, email, cnpj = '', perfil = ''):
        # super().__init__(nome ,whatsapp, endereco, email)
        # self.id = id
        self.nome = nome
        self.whatsapp = whatsapp
        self.endereco = endereco
        self.email = email
        # self.hash_pwd = hash_pwd

        self.cnpj = cnpj
        self.perfil = perfil ## perfil do estabelecimento nas redes sociais
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, nome = None, whatsapp = None, endereco = None, email = None, perfil = None, cnpj = None):
        if nome != None: self.nome = nome
        if whatsapp != None: self.whatsapp = whatsapp
        if endereco != None: self.endereco = endereco
        if email != None: self.email = email
        if perfil != None: self.perfil = perfil
        if cnpj != None: self.cpnj = cnpj

    
    @classmethod
    def find_by_id(cls, id):
        qry = cls.query.filter_by(id = id)
        try:
            result = qry.first()
        except:
            return None
        return result

    @classmethod
    def search_all(cls):
        return cls.query.all()

    def toDict(self):
        return {'nome': self.nome, 'whatsapp': self.whatsapp, 'endereco': self.endereco, 'email': self.email, 'perfil': self.perfil, 'cnpj': self.cnpj}

    

class CandidatoModel(db.Model):
    __tablename__ = 'candidato'

    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(80))
    whatsapp = db.Column(db.Integer())
    endereco = db.Column(db.String(100))
    email = db.Column(db.String(40))
    descricao = db.Column(db.String(500))
    
    def __init__(self, nome, whatsapp, endereco, email, descricao = ''):
        self.nome = nome
        self.whatsapp = whatsapp
        self.endereco = endereco
        self.email = email
        self.descricao = descricao

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,nome = None, whatsapp = None, endereco = None, email = None, descricao = None):
        if not (nome == None or nome == ''): self.nome = nome
        if not (whatsapp == None or whatsapp == ''): self.whatsapp = whatsapp
        if not (endereco == None or endereco == ''): self.endereco = endereco
        if not (email == None or email == ''): self.email = email
        if not (nome == None or nome == ''): self.descricao = descricao

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        qry = cls.query.filter_by(id = id)
        try:
            result = qry.first()
        except:
            return None
        return result

    @classmethod
    def search_all(cls):
        return cls.query.all()
    
    def toDict(self):
        return {'nome': self.nome, 'whatsapp': self.whatsapp, 'endereco': self.endereco, 'email': self.email, 'descricao' : self.descricao}
