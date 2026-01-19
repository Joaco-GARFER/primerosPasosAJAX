function palabras(){
   const palabrasAzar= document.getElementById('palabrasAzar').value;
     fetch("/server",  {    
           method: "POST",
           headers:{ 
            "Content-Type": "application/json" 
            },      
            body: JSON.stringify({  
               palabrasAzar: palabrasAzar
            })
     })
   
     .then (res => res.json())
     .then (dataServer =>{
        document.getElementById("respuestaServer").textContent=dataServer.mensaje
     }

     )
}