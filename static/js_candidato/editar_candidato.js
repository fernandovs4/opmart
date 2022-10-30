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
        setTimeout(
          
          alert("Perfil alterado com sucesso! Você será redirecionado pro seu perfil")
          
          , 3000
        )
        setTimeout(
          
          window.location.href = "perfil-candidato"
          
          , 2000
        )

        
       

  
  
      });
     
      
    })})