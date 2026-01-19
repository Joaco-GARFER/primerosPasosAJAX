from flask import redirect, render_template, request, Flask, jsonify
app=Flask(__name__)
movimientos_saldo=[]
saldo_Mov=0
movimientos_En_Negatvo=[]

@app.route('/')
def home():
    return render_template('EJ5-AJAX.html')

@app.route("/banco", methods=['POST'])
def operaciones():
  global movimientos_saldo
  global saldo_Mov
  global movimientos_En_Negatvo
  dataEntry = request.json
  saldoPrimero = float(dataEntry['saldoInicial'])
  accion= dataEntry['accion']
  
  if accion == 'depositar':
    saldo_Mov+=saldoPrimero
    
  elif accion in ['retirar', 'transferir']:
       saldo_Mov-=saldoPrimero
       if saldo_Mov < 0:
           movimientos_En_Negatvo.append({
               'mensaje': 'USTED NO PUEDE REALIZAR ESTA OPERACION POR QUE NO POSEE DINERO EN SU CUENTA',
               'accion': accion,
               'saldo': saldoPrimero,
                'monto': saldo_Mov
           })
                 
  movimientos_saldo.append({
        "accion": accion.capitalize(),
        'monto': saldoPrimero,
        "saldo": saldo_Mov                 
        
    })
  return jsonify ({
      'movimientos':  movimientos_saldo,
      'negativos': movimientos_En_Negatvo
      })

if __name__ == '__main__':
    app.run(debug=True)


        