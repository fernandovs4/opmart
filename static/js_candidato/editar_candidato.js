$(document).ready(function () {
    
    // $("#form_editar").submit(function (event) {
      
    //   event.preventDefault();

  
    //   var settings = {
    //     "url": "http://localhost:5000/candidato/1",
    //     "method": "PUT",
    //     "timeout": 0,
    //     "headers": {
    //       "Content-Type": "application/json"
    //     },
    //     "data": JSON.stringify({
    //       "nome": $("#nome").val(),
    //       "whatsapp" : $("#whatsapp").val(),
    //       "endereco" : $("#endereco").val(),
    //       "email" : $("#email").val(),
         


    //     }),
    //   };
      
    //   $.ajax(settings).done(function (response) {
    //     console.log(response);

  
  
    //   });
     
      
    // });

    $("#teste").click(function (event) {
      event.preventDefault();
      console.log("teste");
      // print data from form
      console.log($("#nome").val());
      console.log($("#whatsapp").val());
      console.log($("#endereco").val());
      console.log($("#email").val());

      // send data to server
      $.ajax({
        url: "http://localhost:5000/candidato/1",
        type: "PUT",
        data: JSON.stringify({
          "nome": $("#nome").val(),
          "whatsapp" : $("#whatsapp").val(),
          "endereco" : $("#endereco").val(),
          "email" : $("#email").val(),
        }),
        contentType: "application/json",
        success: function (result) {
          console.log(result);
        },
        error: function (error) {
          console.log(error);
        },
      });
      // redirect to home page
      window.location.href = "http://localhost:5000/perfil-candidato";
    });



  
    // make a get request to get the data
    $.get("http://localhost:5000/candidato/1", function (data) {
      console.log(data);
      // set the values of the input fields
      $("#nome").val(data.nome);
      $("#whatsapp").val(data.whatsapp);
      $("#endereco").val(data.endereco);
      $("#email").val(data.email);

    });

  });
