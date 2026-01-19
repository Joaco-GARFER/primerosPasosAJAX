# ↓ ESO SE LLAMA "IMPORTACION DE COMPONENTES DEL FRAMEWORK DE FLASK" sirve para
#   habilitar distintas funcionalidades del backend web
from flask import redirect, Flask, render_template, jsonify, request
import re

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("EJ1.html")

#------PROCESO LOS DATOS QUE ME MANDÓ JS------#
@app.route('/validar', methods=['POST'])
def mov():
    dataEntry= request.json #LEE EL BODY DEL REQUEST, INTERPRETA EL JSON, LO CONVIERTE EN DICT EN PYTHON. 
    nombre = dataEntry["nombre"]
    soloTexto =  r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$' #RAGEX
    
    if nombre.replace(" ", "").isalpha() and len(nombre) > 3:
        return jsonify({"mensaje" : "Nombre Válido"}) # CONVIERTE UN DICT DE PYTHON EN JSON, AGREGA HEADERS CORRECTOS AUTOMATICAMENTE, ES LO QUE AJAX ESPERA RECIBIR.
    else:
        return jsonify({"mensaje": "Nombre Inválido"}) #HACEMOS RETURN JSONIFY DEBIDO A QUE NO PUEDO MANDAR UN DICT DE PYTHON, NO PUEDO RETORNAR ESO.



if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    #¿Qué hace jsonify técnicamente?
      #jsonify hace 3 cosas juntas:
        #Convierte el dict/list de Python a texto JSON
            #Setea el header correcto:
            #Content-Type: application/json
            #Devuelve un Response HTTP válido
            #O sea:
            #return jsonify({
            # "saldo": saldo_actual,
            #"movimientos": movimientos
            #})
            #Equivale conceptualmente a decir:
            #“Tomá este objeto Python, serializalo a JSON y mandalo bien formado al frontend”