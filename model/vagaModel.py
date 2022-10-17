from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db

class Vaga(db.model):
    id_vaga = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    descricao_vaga = db.Column(db.String(500))
    valor_da_vaga = db.Column(db.Integer)
    endereco = db.Column(db.String(500))
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
