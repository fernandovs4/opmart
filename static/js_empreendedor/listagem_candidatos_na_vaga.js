
var vagas_empreendedor = {
    "url": "http://localhost:5000/empreendedor/1/vagas/" + str(window.location.hostname()),
    "method": "GET",
    "headers": {
        "Content-Type": "application/json"
    }};

    $.ajax(vagas_empreendedor).done(function (response) {
        console.log(response);
        for (id in response) {
            

            $("#listagem_vagas").append("<ul id= ul_resp_vagas"+ String(id) +"></ul>")
            $("#ul_resp_vagas"+String(id)).append("<li><a href =" + "/listagem_candidatos_na_vaga.html" + "> nome:" + String(response[id]['nome']) + "</a></li>")
            $("#ul_resp_vagas"+String(id)).append("<li>whatsapp:" + String(response[id]['whatsapp']) + "</li>")
            $("#ul_resp_vagas"+String(id)).append("<li>endereco:" + String(response[id]['endereco']) + "</li>")
            $("#ul_resp_vagas"+String(id)).append("<li>email:" + String(response[id]['email']) + "</li>")}
        

    });
