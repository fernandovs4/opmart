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
  
 
        for (id in response) {
        //   $("#ul-resp"+String(i)).remove()

          $("#feed-col").append("<ul id= ul-resp"+ String(id) +"></ul>")
          $("#ul-resp"+String(id)).append("<li>nome:" + String(response[id]['nome']) + "</li>")
          $("#ul-resp"+String(id)).append("<li>descrição:" + String(response[id][' descricao']) + "</li>")
          $("#ul-resp"+String(id)).append("<li>valor:" + String(response[id]['valor_vaga']) + "</li>")}
         
  
})})
  
  
    //   });
    // });
    
//   


