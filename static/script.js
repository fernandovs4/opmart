$(document).ready(function () {

  
      var settings = {
        "url": "http://localhost:5000/vaga",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
          },
        
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response)
        alert('banana');
 
        // for (id in response) {
        // //   $("#ul-resp"+String(i)).remove()

        //   $("#feed").append("<ul id= ul-resp "+ String(response[id]) +"</ul>")
        //   $("#ul-resp"+String(i)).append("<li>nome:" + String(response[id]['nome']) + "</li>")
        //   $("#ul-resp"+String(i)).append("<li>descrição:" + String(response[id]['descricao']) + "</li>")
        //   $("#ul-resp"+String(i)).append("<li>valor:" + String(response[id]['valor']) + "</li>")
        //   $("#ul-resp"+String(i)).append("<li>endereço:" + JSON.stringify(response[id]['endereco'] + "</li>"))
  
})})
  
  
    //   });
    // });
    
//   


