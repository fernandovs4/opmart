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
      
        {

          $("#vagas_em_destaque").text(
          "<div class='item'>\
              <div class='service-item'>\
                <div class='icon'>\
                  <img src='assets/images/service-icon-02.png'>\
                </div>\
                <h4>Fernando Lindão</h4>\
                <p>Breve descrição.</p>\
              </div>\
          </div> "
        
          
          )}}})})

