$(document).ready(function (){
    var vagas_empreendedor = {
        "url": "http://localhost:5000/empreendedor/1/vagas",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
        }};
    
        $.ajax(vagas_empreendedor).done(function (response) {
            console.log(response);
            for (id in response) {
    
                $("#listagem_vagas").append("<ul id= ul-resp_vagas"+ String(id) +"></ul>")
                $("#ul-resp_vagas"+String(id)).append("<li><a href ="  + id + "/listagem_candidatos_na_vaga.html" + "> nome:" + String(response[id]['nome']) + "</a></li>")
                $("#ul-resp_vagas"+String(id)).append("<li>descrição:" + String(response[id][' descricao']) + "</li>")
                $("#ul-resp_vagas"+String(id)).append("<li>valor:" + String(response[id]['valor_vaga']) + "</li>")}
           
    
        });
    })