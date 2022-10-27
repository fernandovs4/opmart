from flask_restful import Resource
from flask import request, jsonify
from model.pessoasModel import EmpreendedorModel

class ListaEmpreendedor(Resource):
    def get(self):
        todos_empreendedores  = EmpreendedorModel.search_all()
    
        dic = {}
        for empreendedor in todos_empreendedores:
            dic[empreendedor.id] = empreendedor.toDict()

        return dic

    def post(self):
        corpo = request.get_json( force=True )

        empreendedor = EmpreendedorModel(**corpo)
        try:
            empreendedor.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um empreendedor na base."}, 500

        return empreendedor.toDict(), 201


class Empreendedor(Resource):

    def get(self, id):
        try:
            empreendedor = EmpreendedorModel.find_by_id(id = id)
        except:
            return {'erro' : 'Não foi possivel buscar o empreendedor em questão.'}, 500

        if empreendedor:
            return empreendedor.toDict(), 200
        else: 
            return {'erro' : 'Não existe registro desse perfil.'}, 404

    def post(self, id):

        empreendedor = EmpreendedorModel.find_by_id(id)
        if empreendedor:
            return {"erro" : "Já existe um empreendedor com esse registro."}, 400
        else:
            corpo = request.get_json( force=True )

            empreendedor = EmpreendedorModel(id ,**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
            try:
                empreendedor.save()
            except:
                return {"erro":"Ocorreu um erro interno ao tentar inserir um empreendedor (DB)"}, 500
            

            return empreendedor.toDict(), 201
        
    def put(self, id):
        empreendedor = EmpreendedorModel.find_by_id(id)
       
        if empreendedor:
            corpo = request.get_json(force=True)
     
            try:
                empreendedor.update(**corpo)
             
                empreendedor.save()
            except:
                return {'erro' : 'Falha ao atualizar os dados de registro do empreendedor.'}, 500
        else:
            return {"erro" : "Registro de empreendedor não encontrado."}, 404

        return empreendedor.toDict(), 200

    def delete(self, id):
        empreendedor = EmpreendedorModel.find_by_id(id)

        if empreendedor:
            try:
                empreendedor.delete()
            except:
                return {"erro" : "Falha ao deletar registro de empreendedor da base."}, 500
            return {'mensagem' : 'Registro de empreendedor deletado da base.'}, 200
        
        return {'erro' : "Regsitro de empreendedor não encontrado na base"}, 404

        