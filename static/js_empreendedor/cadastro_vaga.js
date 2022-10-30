$(document).ready(function () {


     var settings0 = {
    "url": "http://localhost:5000/empreendedor/1",
    "method": "GET",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/json"
    },}

    $.ajax(settings0).done(function(response0){
      $("#nome_empreendedor_home").text(response0['nome']

        )
  
    })
      
      
        

     
      $("#contact").submit(function (event) {
        event.preventDefault();
        var settings = {
          "url": "http://localhost:5000/vaga",
          "method": "POST",
          "timeout": 0,
          "headers": {
            "Content-Type": "application/json"
          },
          "data": JSON.stringify({
            "nome": $("#nome").val(),
            "descricao" : $("#descricao").val(),
            "valor" : parseInt($("#valor").val()),
            "endereco": $("#endereco").val(),
            "empreendedor_id" : 1,
           
    
    
          })
          



        }
        $.ajax(settings).done(function (response) {
          alert("Vaga cadastrada com sucesso!")
          setTimeout(
          window.location.replace("home-empreendedor", "minhas-vagas"), 2000)
          
          
          console.log(response)
    
        })
      
      



      }
      
      
      
      ) })
  
 
  


         













     
  
   
    