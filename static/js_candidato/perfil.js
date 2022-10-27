$(document).ready(function () {

  
    var setting = {
        "url": "http://localhost:5000/candidato/1",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
        }};

        $.ajax(setting).done(function (response) {
            console.log(response);
            // $("#nome_candidato").append("<h1 id = um > " +  "</h1><br>");
            $("#nome_candidato").append(String(response['nome']) + "<br>");
            $("#nome_candidato").append("<p>" + String(response['email']) + "</p>");
           
    
        });

      
  
   


    }

    // listagem das vagas
    

    

   )