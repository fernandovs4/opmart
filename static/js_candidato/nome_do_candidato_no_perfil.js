// Esse código é só pra colocar o nome do candidato lá no perfil dele no "bem vindo novamente<Nome do candidato>"


    var settings = {
        "url": "http://localhost:5000/candidato/1",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
          },
        
      };
      
      $.ajax(settings).done(function (response) {
        $("#nome_do_candidato").append(response["nome"])
    
        console.log(response)}
        )


