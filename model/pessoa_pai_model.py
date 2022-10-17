from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db

class Pessoa(db.Model):
  
    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(80))
    whatsapp = db.Column(db.Integer())
    endereco = db.Column(db.String())
    email = db.Column(db.String())
    # hash_pwd = db.Column(db.String(100))
   

    def __init__(self , nome, whatsapp, endereco, email, hash_pwd = ''):
        self.nome = nome
        self.whatsapp = whatsapp
        self.endereco = endereco
        self.email = email
        self.hash_pwd = hash_pwd
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    
    @classmethod
    def search_all(cls):
        return cls.query.all()
    
    def toDict(self):
        return {"nome": self.nome, "whatsapp": self.whatsapp, "endereco": self.endereco, "email": self.email, "hash_pwd": self.hash_pwd}



class Empreendedo(db.Model, Pessoa):
    __tablename__ = 'empreendedor'
    id_empreendedor= db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(500))
    email = db.Column(db.String(100))
    cnpj= db.Column(db.String(100))
    perfil= db.Column(db.String(100))
 
    def __init__(self, nome ,whatsapp, endereco, email, cnpj = '', perfil = ''):
        super().__init__(nome ,whatsapp, endereco, email)
        self.cnpj = cnpj
        self.perfil = perfil ## perfil do estabelecimento nas redes sociais
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, novo_nome = None, novo_whatsapp = None, novo_endereco = None, novo_email = None, novo_perfil = None ):
        if novo_nome != None : self.nome = novo_nome
        if novo_whatsapp != None : self.whatsapp = novo_whatsapp
        if novo_endereco != None : self.endereco = novo_endereco
        if novo_email != None : self.email = novo_email
        if novo_perfil != None : self.perfil = novo_perfil

    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id)

    @classmethod
    def search_all(cls):
        return cls.query.all()

    def toDict(self):
        return {'nome': self.nome, 'whatsapp': self.whatsapp, 'endereco': self.endereco, 'email': self.email, 'perfil': self.perfil, 'cnpj': self.cnpj, 'id_empreendedor':self.id_empreendedor}

    

class Trabalhador(db.Model, Pessoa):
    __tablename__ = 'trabalhador'
    id_trabalhador= db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    whatsapp = db.Column(db.Integer)
    endereco = db.Column(db.String(500))
    email = db.Column(db.String(100))
    
    def __init__(self, nome ,whatsapp, endereco, email):
        super().__init__(nome ,whatsapp, endereco, email)
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,nome = None, whatsapp = None, endereco = None, email = None ):
        if nome != None: self.nome = nome
        if whatsapp != None: self.whatsapp = whatsapp
        if endereco != None: self.endereco = endereco
        if email != None: self.email = email

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id)

    @classmethod
    def search_all(cls):
        return cls.query.all()
    
    def toDict(self):
        return {'nome': self.nome, 'whatsapp': self.whatsapp, 'endereco': self.endereco, 'email': self.email,}

class Vaga(db.model):
    id_vaga = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    descricao_vaga = db.Column(db.String(500))
    valor_da_vaga = db.Column(db.Integer)
    empreendedor_id = db.Column(db.Integer, db.ForeignKey('empreendedor.id_empreendedor') )
    empreendedor = db.relationship('Empreendedor', foreign_keys = empreendedor_id)


    def __init__(self, nome ,  descricao_vaga, valor_da_vaga,  empreendedor_id, trabalhador_id ):
        self.nome = nome
        self.descricao_vaga = descricao_vaga
        self.valor_da_vaga = valor_da_vaga
        self.empreendedor_id = empreendedor_id
        self.trabalhador_id = trabalhador_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, novo_nome = None, nova_descricao_vaga = None, novo_valor_vaga = None):
        if novo_nome != None : self.nome = novo_nome
        if nova_descricao_vaga != None:  self.descricao_vaga = nova_descricao_vaga
        if novo_valor_vaga != None: self.valor_da_vaga = novo_valor_vaga
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id)
    
    @classmethod
    def search_all(cls):
        return cls.query.all()

    def toDict(self):
        return {'nome': self.nome, ' descricao_vaga' : self.descricao_vaga, 'valor_vaga': self.valor_da_vaga, 'empreendedor_id': self.empreendedor_id, 'trabalhador_id': self.trabalhador_id}

    
    






 

    

        





