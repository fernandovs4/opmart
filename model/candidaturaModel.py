from sqlalchemy import ForeignKey
from model.sql_alqhemy_para_db import db

class Candidatura(db.Model):
    data = db.Column(db.Date)

    vaga_id = db.Column(db.Integer, db.ForeignKey('vaga.vaga_id'))
    vaga = db.relationship('Vaga', foreign_keys = vaga_id)

    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id_candidato') )
    candidato = db.relationship('Candidato', foreign_keys = candidato_id)