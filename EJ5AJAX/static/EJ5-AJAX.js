function operanDing(accion){
    const saldoInicial = document.getElementById('saldoInicial').value;

    if (saldoInicial === "" || saldoInicial < 0){
        alert('Debe ingresar un Saldo Inicial positivo');
        return
    }

    fetch("/banco", {
       method:'POST',
        headers:{ 
            "Content-Type": "application/json" 
            },
            body: JSON.stringify({  
              saldoInicial:saldoInicial,
              accion:accion
            })
    })

.then(res => res.json())
.then(data => {

        // ===== LISTA DE OPERACIONES NEGATIVAS =====
        const listaNegativa = document.getElementById('NEGATIVA');
        listaNegativa.innerHTML = "";

        if (data.negativos) {
            data.negativos.forEach(neg => {
                const li = document.createElement("li");
                li.textContent = `${neg.mensaje} | Operación: ${neg.accion} | Saldo Actual: $${neg.monto}`;
                listaNegativa.appendChild(li);
            });
        }

        // ===== LISTA DE MOVIMIENTOS NORMALES =====
        const lista = document.getElementById('lista');
        lista.innerHTML = "";

        if (data.movimientos) {
            data.movimientos.forEach(mov => {
                const li = document.createElement("li");
                li.textContent = `Operación: ${mov.accion} | Monto: $${mov.monto} | Saldo: $${mov.saldo}`;
                lista.appendChild(li);
            });
        }

    });
}
