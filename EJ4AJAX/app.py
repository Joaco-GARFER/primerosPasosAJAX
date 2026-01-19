from flask import redirect, render_template, request, jsonify, Flask
app = Flask(__name__)
movimientos=[]
acumulacion=0

@app.route('/')
def home():
    return render_template('EJ4-AJAX.html')


@app.route('/gastos', methods=['POST'])
def controlGastos():
    global acumulacion
    dataEntry = request.json
    monto = float(dataEntry['monto'])
    tipo_de_gasto = dataEntry['tipoDeGasto']
    
    if tipo_de_gasto == 'Supermercado':
    
        acumulacion+=monto
        movimientos.append({
        "tipo": tipo_de_gasto.capitalize(), # → Devuelve una nueva cadena con: la primera letra en mayúscula el resto en minúscula No modifica el string original.
         "monto": monto,  #Es un método y se usa porqué accion viene desde el formulario en formato minuscula y lo queremos mostrar prolijo.                               
         'acumulacion': acumulacion 
        
    })
        return jsonify ({
            "mensaje": 'Gastos: ',
            'movimientos': movimientos})
    elif tipo_de_gasto == 'Hipoteca':
        acumulacion+=monto
        movimientos.append({
       'tipo': tipo_de_gasto.capitalize(),
        'monto': monto,
        'acumulacion' : acumulacion
        })
        return jsonify ({
            "mensaje": 'Gastos: ',
            'movimientos': movimientos})
        
    elif tipo_de_gasto == 'Luz':
        acumulacion+=monto
        movimientos.append({
       'tipo': tipo_de_gasto.capitalize(),
        'monto': monto,
        'acumulacion': acumulacion
        })
        return jsonify ({
            "mensaje": 'Gastos: ',
            'movimientos': movimientos})
    elif tipo_de_gasto == 'Agua':
        acumulacion+=monto
        movimientos.append({
       'tipo': tipo_de_gasto.capitalize(),
        'monto': monto,
        'acumulacion': acumulacion
        })
        return jsonify ({
            "mensaje": 'Gastos: ',
            'movimientos': movimientos})
    elif tipo_de_gasto == 'Gas':
        acumulacion+=monto
        movimientos.append({
       'tipo': tipo_de_gasto.capitalize(),
        'monto': monto,
        'acumulacion': acumulacion
        })
        return jsonify ({
            "mensaje": 'Gastos:',
            'movimientos': movimientos})
        
        
        
        
        
if __name__ == '__main__':
    app.run(debug=True)