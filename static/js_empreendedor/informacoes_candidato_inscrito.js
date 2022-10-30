$(document).ready(function () {
    const params = new URLSearchParams(window.location.search)
  
    var settings = {
      "url": "http://localhost:5000/candidato/" + params.get('id'),
      "method": "GET",
      "headers": {
          "Content-Type": "application/json"
        },
      
    };

    
    $.ajax(settings).done(function (response) {
        
        
            
            $("#detalhe_do_candidato").html("\
            <br>\
                            <p>Nome do candidato: " + response["nome"] + "\
                          <p>Telefone: " + response["whatsapp"] + "</p>\
                          <p>Endereço: " + response["endereco"] +"</p>\
                          <p>Email: " + response["email"] +"</p>\
                          <p>Descrição: " + response["descricao"] + "</p>\
                ")
        
        
      

     })}
    )


