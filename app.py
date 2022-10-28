
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.sql_alqhemy_para_db import db
from resource.empreendedor_rotas import Empreendedor, ListaEmpreendedor
from resource.candidato_rotas import Candidato, ListaCandidato
from resource.vaga_rotas import Vaga, ListaVaga, Empreendedor_id_vagas, Empreendedor_id_vaga_id
from resource.candidatura_rotas import Candidato_id_vagas, Empreendedor_id_vaga_id_candidatos, Candidato_id_vaga_id
from flask_cors import CORS



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


@app.route("/") #home
def hello_world():
    return render_template('home.html')

@app.route("/login-usuario")
def rota_login_candidato_():
    return render_template("candidato/login_candidato.html")

@app.route("/login-empreendedor")
def rota_login_empreendedor():
    return render_template("empreendedor/login_empreendedor.html")

@app.route("/home-candidato")
def home_cantidato():
    return render_template("candidato/home_candidato.html")

@app.route("/perfil-candidato")
def perfil_cantidato():
    return render_template("candidato/perfil_candidato.html")

@app.route("/vagas-candidato")
def rota_vagas_cantidato():
    return render_template("candidato/vagas_candidato.html")

@app.route("/editar-candidato")
def rota_editar_cantidato():
    return render_template("candidato/editar_candidato.html")

@app.route("/detalhe-vaga")
def rota_detalhamento_de_vaga():
    return render_template("geral/detalhe_vaga.html")

@app.route("/listagem-vagas")
def rota_listagem_candidato():
    return render_template("geral/feed_vagas.html")

@app.route("/detalhe-candidato")
def rota_detalhamento_de_candidato():
    return render_template("empresa/detalhe_candidato.html")

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
api.add_resource(Empreendedor_id_vaga_id, '/empreendedor/<int:id_empreendedor>/vaga/<int:id_vaga>/')

if __name__ == '__main__':
    db.init_app(app)
 
    app.run(debug= True)
