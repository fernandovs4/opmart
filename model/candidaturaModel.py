from datetime import date, datetime
from unittest import result
from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db
from model.pessoasModel import CandidatoModel
from model.vagaModel import VagaModel

class CandidaturaModel(db.Model):
    __tablename__ = 'candidatura'

    id = db.Column(db.Integer(), primary_key = True)

    data = db.Column(db.Date)

    vaga_id = db.Column(db.Integer, db.ForeignKey('vaga.id'))
    vaga = db.relationship('VagaModel', foreign_keys = vaga_id)

    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id') )
    candidato = db.relationship('CandidatoModel', foreign_keys = candidato_id)

    def __init__(self, id_vaga, id_candidato):
        self.vaga_id = id_vaga
        self.candidato_id = id_candidato
        self.data = date.today()#.strftime("%d/%m/%Y")

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_by_candidato_id(cls, id):
        qry = cls.query.filter_by(candidato_id = id)
        try:
            result = qry.all()
        except:
            return None
        return result

    @classmethod
    def find_by_vaga_id(cls, id):
        qry = cls.query.filter_by(vaga_id = id)
        try:
            result = qry.all()
        except:
            return None
        return result

    @classmethod
    def find_candidatura(cls, id_candidato, id_vaga):
        qry = cls.query.filter_by(vaga_id = id_vaga, candidato_id = id_candidato)
        try:
            result = qry.first()
        except:
            return None
        return result
    
    @classmethod
    def search_all(cls):
        return cls.query.all()
