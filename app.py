from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.sql_alqhemy_para_db import db
# from model.pessoasModel import 
from resource.empreendedor_rotas import Empreendedor, ListaEmpreendedor
from resource.candidato_rotas import Candidato, ListaCandidato
from resource.vaga_rotas import Vaga, ListaVaga


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/opmart.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
#https://docs.sqlalchemy.org/en/14/core/engines.html
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():
    return {"Estado": "Hello world"}, 200

api.add_resource(Empreendedor, '/empreendedor/<int:id>')
api.add_resource(ListaEmpreendedor, '/empreendedor')
api.add_resource(Candidato, '/candidato/<int:id>')
api.add_resource(ListaCandidato, '/candidato')
api.add_resource(Vaga, '/vaga/<int:id>')
api.add_resource(ListaVaga, '/vaga')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug= True)
