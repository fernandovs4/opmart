$(document).ready(function () {

    
    
    $("#form_editar").submit(function (event) {
      
      event.preventDefault();

  
      var settings = {
        "url": "http://localhost:5000/candidato",
        "method": "POST",
        "timeout": 1,
        "headers": {
          "Content-Type": "application/json"
        },
        "data": JSON.stringify({
          "nome": $("#nome").val(),
          "whatsapp" : $("#whatsapp").val(),
          "endereco" : $("#endereco").val(),
          "email" : $("#email").val(),
          "descricao" : $("#descricao").val(),
         


        }),
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        setTimeout(
          
          alert("Cadastro efetuado com sucesso! Você será redirecionado pra área de login")
          
          , 3000
        )
        setTimeout(
          
          window.location.href = "login-candidato"
          
          , 2000
        )

        
       

  
  
      });
     
      
    })})