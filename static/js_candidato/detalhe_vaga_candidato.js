
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
        console.log(response)
        for (id in response) {

            if (id == params.get('id')){
                inscrito_na_vaga = true
            }

        }
        if (inscrito_na_vaga) {
            $("#div_candidatar-se").hide();
        }
        else {

            $("#botao_candidartar-se").click( function (event) {
            event.preventDefault();

            var settings2 = {
                "url": "http://localhost:5000/candidato/" + id_candidato + "/vagas",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify({
                  "vaga_id": params.get('id')
                }),
              };
              
              $.ajax(settings2).done(function (response2) {
                
              });
              window.location.reload()
            //   window.location.replace = "localhost:5000/listagem-vagas"
                                                            }
            
                                            )
        }
                                                })
                                }
                            
                )