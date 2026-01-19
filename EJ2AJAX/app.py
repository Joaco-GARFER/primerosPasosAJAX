from flask import redirect, Flask, render_template, jsonify, request
 

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('EJ2-AJAX.html')     

@app.route('/server', methods=['POST'])
def validPalabras():
    
    dataEntry= request.json
    
    
    palabrasAzar= dataEntry['palabrasAzar']
    if palabrasAzar.replace(" ", "").isalpha() and len(palabrasAzar) > 3:
     listaPalabras = palabrasAzar.split()
     palabrasUnicas = set(listaPalabras)# SET: elimina palabras repetidas automáticamente
       

     if len(listaPalabras) != len(palabrasUnicas):
        return jsonify({
            "mensaje": "Hay palabras repetidas"
        })
     return jsonify({'mensaje': listaPalabras})
    else:
     return jsonify({
        "mensaje": "Texto inválido (solo letras y espacios, más de 3 caracteres)"
    })
   
if __name__ == '__main__':
    app.run(debug=True)
    