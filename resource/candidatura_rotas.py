from flask_restful import Resource
from flask import request, jsonify
from model.candidaturaModel import CandidaturaModel
from model.vagaModel import VagaModel
from model.pessoasModel import EmpreendedorModel, CandidatoModel

class Candidato_id_vagas(Resource):

    ## Listagem das vagas as quais o candidato se inscreveu
    def get(self, id):
        try:
            candidaturas = CandidaturaModel.find_by_candidato_id(id = id)
        except:
            return {'erro' : 'Não foi possivel buscar as vagas em questão.'}, 500

        if candidaturas:
            dic = {}
            for candidatura in candidaturas:
                vaga = VagaModel.find_by_id(id = candidatura.vaga_id)
                dic[vaga.id] = vaga.toDict()

            return dic
        else: 
            return {'erro' : 'O candidato ainda não realizou inscrições.'}, 404


    ## Realização da inscrição do candidato numa vaga
    def post(self, id):

        ## requisição deve conter id_vaga
        corpo = request.get_json( force=True )

        candidatura = CandidaturaModel.find_candidatura(id_candidato= id,**corpo)
        if candidatura: ## caso seja encontrada uma candidatura do candidato para aquela vaga, não será possível criar uma nova.
            return {"erro" : "Candidato já inscrito na vaga."}
        candidatura = CandidaturaModel(id_candidato= id,**corpo)
        try:
            candidatura.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um candidatura na base."}, 500

        return {"mensagem" : "Inscrição realizada na vaga com sucesso."}, 201

class Candidato_id_vaga_id(Resource):

    def delete(self, id_candidato, id_vaga):
        candidatura = CandidaturaModel.find_candidatura(id_candidato= id_candidato, id_vaga= id_vaga)
        if candidatura:
            try:
                candidatura.delete()
            except:
                return {"erro" : 'Falha ao deletar registro da candidatura da base.'}, 500
            
            return {'mensagem' : 'Registro da candidatura deletado da base.'}, 200

        return {'erro' : 'Registro da candidatura não encontrado na base.'}, 404

class Empreendedor_id_vaga_id_candidatos(Resource):
    def get(self, id_empreendedor, id_vaga):
        vagas_do_empreendedor  = VagaModel.search_by_empreendedor_id(id_empreendedor= id_empreendedor)
        if vagas_do_empreendedor:
            
            try:
                candidaturas = CandidaturaModel.find_by_vaga_id(id = id_vaga)
            except:
                return {"erro", "Falha ao buscar a vaga no banco."}, 500
            if candidaturas:
                dic = {}
                for candidatura in candidaturas:
                    candidato = CandidatoModel.find_by_id(candidatura.candidato_id)
                    dic[candidato.id] = candidato.toDict()

                return dic, 200
            else:
                return {"mensagem" : "Não há candidatos inscritos na vaga"}, 200
        else:
            return {"erro" : "Ainda não há vagas registradas para esse empreendedor."}, 404



