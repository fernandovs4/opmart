from flask_restful import Resource
from flask import request, jsonify
from model.candidaturaModel import CandidaturaModel

class Candidato_id_vagas(Resource):

    ## Listagem das vagas as quais o candidato se inscreveu
    def get(self, id):
        try:
            candidatura = CandidaturaModel.find_by_candidato_id(id = id)
        except:
            return {'erro' : 'Não foi possivel buscar as vagas em questão.'}, 500

        if candidatura:
            return candidatura.toDict(), 200
        else: 
            return {'erro' : 'O candidato ainda não realizou inscrições.'}, 404


    def post(self, id):

        ## requisição deve conter id_vaga
        corpo = request.get_json( force=True )

        candidatura = CandidaturaModel(id_candidato= id,**corpo)
        try:
            candidatura.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um candidatura na base."}, 500

        return candidatura.toDict(), 201

class Candidato_id_vaga_id(Resource):

    def delete(self, id_candidato, id_vaga):
        candidatura = CandidaturaModel.find_candidatura()
        pass