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
           
            $("#vagas_candidato").append(
                              
                "<div class='col-lg-3 align-self-center'>\
                <a href = 'detalhe-vaga?id=" + id + "'>\
                <div class='right-info'>\
                <div class='col-lg-12'>\
                  <div class='info-item'>\
                    <h4>" +   response[id]['nome'] + "</h4>\
                    <p> " + "descrição: " +  response[id]['descricao'] + "</p>\
                    <p> " + "salário: " + response[id]['valor_vaga'] + " </p>\
                    <div id='feed-col' >\
                    </div>\
                  </div>\
                </div>\
              " + "</a> "+ "</div>" 
            )
        }
    });
})
