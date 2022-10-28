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
        let imagem =  "<div class='icon'>\
        <img src=" + '"'+ "{{url_for('static', filename = 'images/service-icon-01.png')}}" + '"' + " >\
      </div>"
  
 
        for (id in response) {
        //   $("#ul-resp"+String(i)).remove()

          $("#feed_vagass").append(
                          
                          "<div class='col-lg-3 align-self-center'>\
                          <a href = 'detalhe-vaga?id=" + id + "'>\
                          <div class='right-info'>\
                          <div class='col-lg-12'>\
                            <div class='info-item'>\
                              <h4>" +   response[id]['nome'] + "</h4>\
                              <p> " + "descrição: " +  response[id]['descricao'] + "</p>\
                              <p> " + "salário: " + response[id]['valor_vaga'] + " </p>\
                              <div id='feed-col' >\
                              </div>\
                            </div>\
                          </div>\
                        " + "</a> "+ "</div>" 






          )
         
        
        }
         
  
})})
  
  

