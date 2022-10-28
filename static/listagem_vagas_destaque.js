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

          $("#owl-service-item owl-carousel").text(
            "<div class='item'>\
            <div class='service-item'>\
              <h4>Cargo da vaga</h4>\
              <p>Breve descrição.</p>\
            </div>\
          </div>"
          )
        }
      }
    }
    )
        })
