
let searchParams = new URLSearchParams(window.location.search)
let param = searchParams.get('id')
console.log(param)

function isEmpty(obj) {
  return Object.keys(obj).length === 0 && obj.constructor === Object;
}

var vagas_empreendedor = {

    
    "url": "http://localhost:5000/empreendedor/1/vaga/" +  param + "/candidatos" ,
    "method": "GET",
    "headers": {
        "Content-Type": "application/json"
    }};

  // Esse vagas_empreendedor_sera verifica se aquela vaga é do empreendedor 1, se nao for ele nao mostra o texto "inscrito na vaga"
var vagas_empreendedor_sera = {

    
    "url": "http://localhost:5000/vaga" ,
    "method": "GET",
    "headers": {
        "Content-Type": "application/json"
    }};

    $.ajax(vagas_empreendedor).done(function (response) {

        
        console.log(response);

        $.ajax(vagas_empreendedor_sera).done(function(response2){
          if (response2[param]["empreendedor_id"] == 1){
            if ( response["mensagem"] != "Não há candidatos inscritos na vaga"){
              for (id in response) {
                  //   $("#ul-resp"+String(i)).remove()
          
                    $("#feed_vag").append(

                                    
                                    "<div class='col-lg-3 align-self-center'>\
                                    <a href = 'perfil-candidato-inscrito?id=" + id +"'" + ">\
                                    <div class='right-info'>\
                                    <div class='col-lg-12'>\
                                      <div class='info-item'>\
                                        <h4>" +   response[id]['nome'] + "</h4>\
                                        <p> " + "nome: " +  response[id]['whatsapp'] + "</p>\
                                        <p> " + "endereco: " + response[id]['endereco'] + " </p>\
                                        <p> " + "email: " + response[id]['email'] + " </p>\
                                        <p> " + "descrição: " + response[id]['descricao'] + " </p>\
                                      </div>\
                                    </div>\
                                    </a>\
                                  </div>"
                                
          
          
          
                    )
                  
                  
                  }}
                  else{
                    $("#inscrito_na_vaga").text("Não há candidatos inscritos nessa vaga")
                  }

          }
          else{
            $("#inscrito_na_vaga").hide()
          }
          

        })
        
           
        

    });
