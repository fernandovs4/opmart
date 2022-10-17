from flask_restful import Resource
from flask import request, jsonify
from imageio import imopen
from model.pessoasModel import Pessoa, Empreendedor, Vaga, Trabalhador




class Empreendedor(Resource):

    def post(nome, whatsapp, endereco, email,cnpj,  perfil):
        corpo = request.get_json( force=True )

        empreendedor = Empreendedor(**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            empreendedor.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um aluno (DB)"}, 500
        

        return empreendedor.toDict(), 201