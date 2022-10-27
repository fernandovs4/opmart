$(document).ready(function () {
    
    $("#form_editar").submit(function (event) {
       
   
      event.preventDefault();

  
      var settings = {
        "url": "http://localhost:5000/empreendedor/1",
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
          "cnpj" : $("#cnpj").val(),
         


        }),
      };
      
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        url_atual = $(location).attr('href');
        a = window.location.pathname()
       
        window.location.replace(a, 'perfil_empreendedor.html')
        console.log(url_atual)
        

  
  
      });
      
     
      
    });
  
    
  
   });
  
    