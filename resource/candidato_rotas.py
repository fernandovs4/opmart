from flask_restful import Resource
from flask import request, jsonify
from model.pessoasModel import CandidatoModel

class ListaCandidato(Resource):
    def get(self):
        todos_candidatos  = CandidatoModel.search_all()
    
        dic = {}
        for candidato in todos_candidatos:
            dic[candidato.id] = candidato.toDict()

        return dic

    def post(self):
        corpo = request.get_json( force=True )

        candidato = CandidatoModel(**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            candidato.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um candidato na base."}, 500

        return candidato.toDict(), 201


class Candidato(Resource):

    def get(self, id):
        try:
            candidato = CandidatoModel.find_by_id(id = id)
        except:
            return {'erro' : 'Não foi possivel buscar o candidato em questão.'}, 500

        if candidato:
            return candidato.toDict(), 200
        else: 
            return {'erro' : 'Não existe registro desse perfil'}, 404

    # def post(self, id):

    #     candidato = CandidatoModel.find_by_id(id)
    #     if candidato:
    #         return {"erro" : "Já existe um candidato com esse registro."}, 400
    #     else:
    #         corpo = request.get_json( force=True )

    #         candidato = CandidatoModel(id ,**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
    #         try:
    #             candidato.save()
    #         except:
    #             return {"erro":"Ocorreu um erro interno ao tentar inserir um candidato (DB)"}, 500
            

    #         return candidato.toDict(), 201
        
    def put(self, id):
        candidato = CandidatoModel.find_by_id(id)
       
        if candidato:
            corpo = request.get_json(force=True)
     
            try:
                candidato.update(**corpo)
             
                candidato.save()
            except:
                return {'erro' : 'Falha ao atualizar os dados de registro do candidato.'}, 500
        else:
            return {"erro" : "Registro de candidato não encontrado."}, 404

        return candidato.toDict(), 200

    def delete(self, id):
        candidato = CandidatoModel.find_by_id(id)

        if candidato:
            try:
                candidato.delete()
            except:
                return {"erro" : "Falha ao deletar registro de candidato da base."}, 500
            return {'mensagem' : 'Registro de candidato deletado da base.'}, 200
        
        return {'erro' : "Regsitro de candidato não encontrado na base"}, 404
