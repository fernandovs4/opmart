from flask_restful import Resource
from flask import request, jsonify
from model.vagaModel import VagaModel

class ListaVaga(Resource):
    def get(self):
        todas_vagas  = VagaModel.search_all()
    
        dic = {}
        for vaga in todas_vagas:
            dic[vaga.id] = vaga.toDict()

        return dic

    def post(self):
        corpo = request.get_json( force=True )

        vaga = VagaModel(**corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            vaga.save()
        except:
            return {"erro":"Ocorreu um erro interno ao tentar inserir um vaga na base."}, 500

        return vaga.toDict(), 201


class Vaga(Resource):

    def get(self, id):
        try:
            vaga = VagaModel.find_by_id(id)
        except:
            return {'erro' : 'Não foi possivel buscar o vaga em questão.'}, 500

        if vaga:
            return vaga.toDict(), 200

        else:
            return {'erro' : 'Não existe registro dessa vaga.'}, 404

    def put(self, id):
        vaga = VagaModel.find_by_id(id)

        if vaga: 
            corpo = request.get_json(force=True)

            try: 
                vaga.update(**corpo)
                vaga.save

            except:
                return {'erro' : 'Falha ao atualizar os dados de registro da vaga.'}, 500

        else:
            return {'erro' : 'Registro de vaga não encontrado.'}, 404

        return vaga.toDict(), 200

    def delete(self, id):
        vaga = VagaModel.find_by_id(id)

        if vaga:
            try:
                vaga.delete()
            except:
                return {"erro" : 'Falha ao deletar registro da vaga da base.'}
            
            return {'mensagem' : 'Registro da vaga deletado da base.'}, 200

        return {'erro' : 'Registro da vaga não encontrado na base.'}, 404
        