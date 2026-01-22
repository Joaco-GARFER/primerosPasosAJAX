function operanDing(accion){
    const saldoInicial = document.getElementById('saldoInicial').value;
    const nombreUser = document.getElementById('nombreUser').value;
    const soloTexto =  /^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$/; //RAGEX

    if (nombreUser === "" || !soloTexto.test(nombreUser)){
        alert('Debe ingresar un Nombre de usario Solo en Letras Sin numeros ni Caracteres Especiales')
        return
    }

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
              accion:accion,
              nombreUser: nombreUser
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
                li.textContent = `${neg.mensaje} | Operación: ${neg.accion}| Realizada por: ${neg.nombre} | Saldo Actual: $${neg.monto}`;
                listaNegativa.appendChild(li);
            });
        }

        // ===== LISTA DE MOVIMIENTOS NORMALES =====
        const lista = document.getElementById('lista');
        lista.innerHTML = "";

        if (data.movimientos) {
            data.movimientos.forEach(mov => {
                const li = document.createElement("li");
                li.textContent = `Operación: ${mov.accion}| Realizada por: ${mov.nombre} | Monto: $${mov.monto} | Saldo: $${mov.saldo}`;
                lista.appendChild(li);
            });
        }

    });
}
