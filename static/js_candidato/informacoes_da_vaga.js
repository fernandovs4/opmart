$(document).ready(function () {
    const params = new URLSearchParams(window.location.search)
  
    var settings = {
      "url": "http://localhost:5000/vaga/" + params.get('id'),
      "method": "GET",
      "headers": {
          "Content-Type": "application/json"
        },
      
    };
    
    $.ajax(settings).done(function (response) {
        var settings2 = {
            "url": "http://localhost:5000/empreendedor/"+ response["empreendedor_id"],
            "method": "GET",
            "headers": {
            "Content-Type": "application/json"
            },
        };
        $.ajax(settings2).done(function (response2) {
            
            $("#detalhe_da_vaga").html("\
            <br>\
      <h4>" + response["nome"] + "</h4>\
                            <p>Nome do empregador: " + response2["nome"] + "\
                          <p>Telefone: " + response2["whatsapp"] + "</p>\
                          <p>Endereço: " + response2["endereco"] +"</p>\
                          <p>Email: " + response2["email"] +"</p>\
                          <p>Salário: " + response["valor_vaga"] + "</p>\
                          <p>Descrição: " + response["descricao"] + "</p>\
                ")
        }
        )
      

     }
    )
})

