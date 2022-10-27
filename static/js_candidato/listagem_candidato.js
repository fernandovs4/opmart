$(document).ready(function (){
var vagas_candidato = {
    "url": "http://localhost:5000/candidato/1/vagas",
    "method": "GET",
    "headers": {
        "Content-Type": "application/json"
    }};

    $.ajax(vagas_candidato).done(function (response) {
        console.log(response);
        for (id in response) {
           

            $("#listagem_vagas").append("<ul id= ul-resp_vagas"+ String(id) +"></ul>")
            $("#ul-resp_vagas"+String(id)).append("<li>nome:" + String(response[id]['nome']) + "</li>")
            $("#ul-resp_vagas"+String(id)).append("<li>descrição:" + String(response[id][' descricao']) + "</li>")
            $("#ul-resp_vagas"+String(id)).append("<li>valor:" + String(response[id]['valor_vaga']) + "</li>")}
       

    });
})