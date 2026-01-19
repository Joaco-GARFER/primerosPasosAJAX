function enviarNombre(){
    const nombre = document.getElementById('nombre').value; //CAPTURAMOS EL DATO, LEE EL VALOR DEL INPUT, SOLO VIVE EN FRONTEND.
 
 
    //---------------ESTA PARTE LE MANDA DATOS AL SERVIDOR------------//   
    fetch("/validar",  {    
         //FETCH ES LA API NATIVA DEL NAVEGADOR PARA HACER HTTP REQUEST,
        //SE COMUNICA CON FLASK SIN RECARGAR LA PAGINA
        //VALIDAR ES LA RUTA DEL BACKEND
           method: "POST",
           headers:{ //METADATO ↓
            "Content-Type": "application/json" // LE AVISAMOS AL SERVIDOR "TE MANDO DATOS EN FORMATO JSON",
            //ESTO ES PARA QUE FLASK USE REQUEST.JSON
            },      
            body: JSON.stringify({  //ACA SE SERIALIZA UN OBJETP JS A TEXTO JSON → "{\"nombre\":\"Juan\"}" ES TEXTO PLANO POR LO TANTO ES VALIDO PARA VIAJAR POR RED.
            nombre: nombre  //ESTE OBJETO JS NO PUEDE VIAJAR MEDIANTE HTTP
            })
  })


  //------------ESTA ES LA PARTE QUE RECIBE LOS DATOS DE FLASK---------//

  .then(res => res.json())// "RES" ES LA RESPUESTA CRUDA DEL SERVIDOR, "RES.JSON" 
  // LEE EL BODY DE LA RESPUESTA Y CONVIERTE EL JSON EN UN OBJETO JS. 
  .then(data=>{ //DATA es solo un nombre de la variable, guarda lo que devuelve flask con jsonify, ya convertido a objeto JavaScript //ya está convertido a objeto pq se crea con res.json.
    document.getElementById("respuesta").textContent=data.mensaje // cambiamos "respuesta" por lo que trajo flask"
  }) //DATA ES EL OBJETO JS QUE FLASK DEVOLVIÓ

}


//Recordemos que la flecha "=>" es una "ARROW FUNCTION" (funcion flecha)