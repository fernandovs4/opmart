from flask_restful import Resource
from flask import request, jsonify
from model.pessoasModel import EmpreendedorModel




class Empreendedor(Resource):

    def get(self, id):
        try:
            empreendedor = EmpreendedorModel.find_by_id(id = id)
        except:
            return {'erro' : 'Não foi possivel buscar o empreendedor em questão.'}, 500

        if empreendedor:
            return empreendedor.toDict(), 200
        else: 
            return {'erro' : 'Não existe registro desse perfil'}, 404

    def post(self, id):
        corpo = request.get_json( force=True )

        
        empreendedor = EmpreendedorModel(id ,**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            empreendedor.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um aluno (DB)"}, 500
        

        return empreendedor.toDict(), 201