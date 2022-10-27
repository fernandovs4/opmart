from flask_restful import Resource
from flask import request, jsonify
from model.vagaModel import VagaModel
from model.candidaturaModel import CandidaturaModel

class ListaVaga(Resource):
    def get(self):
        todas_vagas  = VagaModel.search_all()
    
        if todas_vagas:
            dic = {}
            for vaga in todas_vagas:
                dic[vaga.id] = vaga.toDict()

            return dic, 200
        else: 
            return {"erro" : "Ainda não há vagas cadastradas"}, 404

    def post(self):
        corpo = request.get_json( force=True )
        print(corpo)
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
                return {"erro" : 'Falha ao deletar registro da vaga da base.'}, 500
            
            return {'mensagem' : 'Registro da vaga deletado da base.'}, 200

        return {'erro' : 'Registro da vaga não encontrado na base.'}, 404
        

class Empreendedor_id_vagas(Resource):

    def get(self, id_empreendedor):
        vagas_do_empreendedor  = VagaModel.search_by_empreendedor_id(id_empreendedor= id_empreendedor)
        if vagas_do_empreendedor:
            dic = {}
            for vaga in vagas_do_empreendedor:
                dic[vaga.id] = vaga.toDict()

            return dic, 200
        else:
            return {"erro", "Não há vagas cadastradas no sistema. Cadastre novas vagas para que apareçam aqui."}, 404

class Empreendedor_id_vaga_id(Resource):

    def delete(self, id_empreendedor, id_vaga):
        vagas_do_empreendedor  = VagaModel.search_by_empreendedor_id(id_empreendedor= id_empreendedor)
        for vaga in vagas_do_empreendedor:
            if vaga.id == id_vaga:
                vaga = VagaModel.find_by_id(id)
                try:
                    vaga.delete()
                except:
                    return {"erro" : 'Falha ao deletar registro da vaga da base.'}, 500
                candidaturas = CandidaturaModel.find_by_vaga_id(id= id_vaga)
                for candidatura in candidaturas:
                    candidatura.delete()
                return {"mensagem" : "Vaga deletada com sucesso"}, 200
        return {"erro" : "A vaga não pertence a esse empreendedor."}