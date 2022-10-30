
var id_empreendedor = 1
$(document).ready(function () {
    const params = new URLSearchParams(window.location.search)

    var settings = {
        "url": "http://localhost:5000/empreendedor/" + id_empreendedor +"/vagas",
        "method": "GET",
        "headers": {
            "Content-Type": "application/json"
          },
        
      };
      $.ajax(settings).done(function (response) {
        let dono_da_vaga = false
        console.log(response)
        for (id in response) {

            if (id == params.get('id')){
                dono_da_vaga = true
            }

        }
        if (dono_da_vaga) {
          $("#botao_excluir_vaga").click( function (event) {
            event.preventDefault();

            var settings2 = {
              "url": "http://localhost:5000/empreendedor/" + id_empreendedor +"/vaga/" + params.get('id') ,
              "method": "DELETE",
              "headers": {
                  "Content-Type": "application/json"
                },
              
            };

            
           
              
              $.ajax(settings2).done(function (response2) {
                console.log(response2)
                alert("Vaga deletada com sucesso!!")
              
              });
              setTimeout(function(){ 
                window.location.replace("vagas-empreendedor")
                
            }, 3000);
            

         
              
                                                            })
            
        }
        else {
            $("#div_excluir_vaga").hide();
        }
                                                })
                                }
                            
                )

              