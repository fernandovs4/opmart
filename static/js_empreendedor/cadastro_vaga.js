$(document).ready(function () {

      
        var set = {
          "url": "http://localhost:5000/empreendedor/1",
          "method": "GET",
          "timeout": 0,
          "headers": {
            "Content-Type": "application/json"
          },
          
        }

        $.ajax(set).done(function (resp) {
          $("#nome_empreendedor_home").text(resp['nome'])
          
          console.log(response)
    
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
            "endereco": $("#descricao").val(),
            "empreendedor_id" : 1,
           
    
    
          })
          



        }
        $.ajax(settings).done(function (response) {
          
          
          console.log(response)
    
        })
      
        setTimeout(function () {
          $('#texto').hide(); // "foo" é o id do elemento que seja manipular.
        }, 2500); // O valor é representado em milisegundos.



      }
      
      
      
      ) })
  
 
  


         













     
  
   
    