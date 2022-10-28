
var id_candidato = 1
$(document).ready(function () {
    const params = new URLSearchParams(window.location.search)

    var settings = {
        "url": "http://localhost:5000/candidato/" + id_candidato +"/vagas",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
          },
        
      };
      $.ajax(settings).done(function (response) {
        let inscrito_na_vaga = false

        for (id in response) {

            if (id == params.get('id')){
                inscrito_na_vaga = true
            }

        }
        if (inscrito_na_vaga) {
            $("#")
        }
                                                })
                                }
                            
                )