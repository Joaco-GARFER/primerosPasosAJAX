function operacion(accion){
    const primerNumero = document.getElementById('num1').value; 
    const segundoNumero = document.getElementById('num2').value;

    if (primerNumero === "" || segundoNumero=== ""){
        alert('Debe ingresar un Número')
        return
    }

   fetch('/calculo',{
    method: "POST",
    headers:{ 
            "Content-Type": "application/json" 
            },      
    body: JSON.stringify({  
               accion : accion,
               primerNumero : primerNumero,
               segundoNumero :  segundoNumero
            })
   })
   .then(res => res.json())
   .then( data => {
    document.getElementById("respuesta").textContent = data.mensaje
   })
}