
let searchParams = new URLSearchParams(window.location.search)
let param = searchParams.get('id')
console.log(param)

var vagas_empreendedor = {

    
    "url": "http://localhost:5000/empreendedor/1/vaga/" +  param + "/candidatos" ,
    "method": "GET",
    "headers": {
        "Content-Type": "application/json"
    }};

    $.ajax(vagas_empreendedor).done(function (response) {
        console.log(response);
        for (id in response) {
            //   $("#ul-resp"+String(i)).remove()
    
              $("#feed_vag").append(
                              
                              "<div class='col-lg-3 align-self-center'>\
                              <div class='right-info'>\
                              <div class='col-lg-12'>\
                                <div class='info-item'>\
                                  <h4>" +   response[id]['nome'] + "</h4>\
                                  <p> " + "descrição: " +  response[id]['whatsapp'] + "</p>\
                                  <p> " + "endereco: " + response[id]['endereco'] + " </p>\
                                  <p> " + "email: " + response[id]['email'] + " </p>\
                                  <p> " + "descrição: " + response[id]['descricao'] + " </p>\
                                </div>\
                              </div>\
                            </div>" 
    
    
    
              )
             
            
            }
        

    });
