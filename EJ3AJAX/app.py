from flask import redirect, render_template, request, Flask, jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("EJ3-AJAX.html")

@app.route('/calculo', methods=["POST"])
def controlCalculos():
    global resultado_suma
    dataEntry = request.json
    numeroPrimero =float(dataEntry['primerNumero'])
    numeroSegundo = float(dataEntry['segundoNumero'])#TENER EN CUENTA ACÁ, PASAR A FLOAT O A INT PQ VIENE EN FORMATO DE TEXTO
    
    accion = dataEntry['accion']
    if accion == 'suma':
        resultado_suma = numeroPrimero + numeroSegundo 
        return jsonify ({"mensaje": resultado_suma}) 
    elif accion == 'resta':
        resultado_resta = numeroPrimero-numeroSegundo
        return jsonify ({'mensaje': resultado_resta})
    elif accion == 'multiplicacion':
        resultado_multiplicacion = numeroPrimero*numeroSegundo
        return jsonify ({'mensaje': resultado_multiplicacion})
    elif accion == 'division':
        if numeroSegundo != 0:
         resultado_division = numeroPrimero / numeroSegundo
         return jsonify ({'mensaje': resultado_division})
        else: 
            return jsonify({'mensaje': 'No puede dividir por cero'}) 
    else: 
        return jsonify ({'mensaje': 'Debe elegir una operación a realizar'})


  
if __name__ == '__main__':
    app.run(debug=True)