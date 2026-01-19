function operacion(tipoDeGasto){
    const monto = document.getElementById('monto').value;
    if (monto === "" || monto < 0){
        alert('Revise de haber ingresado un monto, Y que el mismo sea MAYOR a 0')
        return
    }
    fetch("/gastos"  ,{
        method:'POST',
        headers:{ 
            "Content-Type": "application/json" 
            },      
            body: JSON.stringify({  
               tipoDeGasto: tipoDeGasto,
               monto : monto
            })
    })
// en el envío todo ok

.then (res => res.json())
.then (data=>{
document.getElementById('respuestaServer').textContent=data.mensaje;


const lista = document.getElementById('listaMv');
lista.innerHTML = "";

data.movimientos.forEach(mov => {
    const li = document.createElement("li");
    li.textContent = `Gasto de: ${mov.tipo} | Por un Monto de: $${mov.monto}| Total Gastos Acumulados: $${mov.acumulacion}`
    lista.appendChild(li);
    
});


})
    


}