$(document).ready(function () {
    
    $("#form_editar").submit(function (event) {
      
      event.preventDefault();

  
      var settings = {
        "url": "http://localhost:5000/candidato/1",
        "method": "PUT",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/json"
        },
        "data": JSON.stringify({
          "nome": $("#nome").val(),
          "whatsapp" : $("#whatsapp").val(),
          "endereco" : $("#endereco").val(),
          "email" : $("#email").val(),
         


        }),
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);

  
  
      });
     
      
    });
  
    
  
    $("#form_candidato").submit(function (event) {
      
      event.preventDefault();
  
   
  
      var settings = {
        "url": "http://localhost:5000/candidato",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/json"
        },
        "data": JSON.stringify({
          "nome": $("#nome_candidato").val(),
          "whatsapp" : $("#whatsapp_candidato").val(),
          "endereco" : $("#endereco_candidato").val(),
          "email" : $("#email_candidato").val(),

        }),
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        for (id in response) {
    
            $("#feed-col").append("<ul id= ul-resp"+ String(id) +"></ul>")
            $("#ul-resp"+String(id)).append("<li>nome:" + String(response[id]['nome']) + "</li>")
            $("#ul-resp"+String(id)).append("<li>descrição:" + String(response[id][' descricao']) + "</li>")
            $("#ul-resp"+String(id)).append("<li>valor:" + String(response[id]['valor_vaga']) + "</li>")}
  
  
      });
    })});
  
    
  