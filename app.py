from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.sql_alqhemy_para_db import db
from resource.empreendedor_rotas import Empreendedor, ListaEmpreendedor
from resource.candidato_rotas import Candidato, ListaCandidato
from resource.vaga_rotas import Vaga, ListaVaga
from resource.candidatura_rotas import Candidato_id_vagas
from flask_cors import CORS
from resource.vaga_rotas import Vaga, ListaVaga, Empreendedor_id_vagas
from resource.candidatura_rotas import Candidato_id_vagas, Empreendedor_id_vaga_id_candidatos, Candidato_id_vaga_id



# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/opmart.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
CORS(app)
#https://docs.sqlalchemy.org/en/14/core/engines.html
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route("/login_candidato")
def empre():
    return render_template('login_candidato.html')



api.add_resource(Empreendedor, '/empreendedor/<int:id>')
api.add_resource(ListaEmpreendedor, '/empreendedor')
api.add_resource(Candidato, '/candidato/<int:id>')
api.add_resource(ListaCandidato, '/candidato')
api.add_resource(Vaga, '/vaga/<int:id>')
api.add_resource(ListaVaga, '/vaga')
api.add_resource(Candidato_id_vagas, '/candidato/<int:id>/vagas')
api.add_resource(Candidato_id_vaga_id, '/candidato/<int:id_candidato>/vaga/<int:id_vaga>')
api.add_resource(Empreendedor_id_vagas, '/empreendedor/<int:id_empreendedor>/vagas')
api.add_resource(Empreendedor_id_vaga_id_candidatos, '/empreendedor/<int:id_empreendedor>/vaga/<int:id_vaga>/candidatos')


if __name__ == '__main__':
    db.init_app(app)
 
    app.run(debug= True)
