from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db
from model.pessoasModel import EmpreendedorModel



class VagaModel(db.Model):
    __tablename__ = 'vaga'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(500))
    valor = db.Column(db.Integer)
    endereco = db.Column(db.String(500))
    empreendedor_id = db.Column(db.Integer, db.ForeignKey('empreendedor.id') )
    empreendedor = db.relationship('EmpreendedorModel', foreign_keys = empreendedor_id)


    def __init__(self, nome, descricao, valor, endereco, empreendedor_id):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.endereco = endereco
        self.empreendedor_id = empreendedor_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, nome = None, descricao = None, valor = None, endereco = None):
        if nome != None : self.nome = nome
        if descricao != None:  self.descricao = descricao
        if valor != None: self.valor = valor
        if endereco != None: self.endereco = endereco
        
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
        return {'nome': self.nome, ' descricao' : self.descricao, 'valor_vaga': self.valor, 'empreendedor_id': self.empreendedor_id}
