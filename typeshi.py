from flask import Flask, request
import uuid 

app = Flask(__name__)

lista_calculos = []

@app.route("/soma", methods=["POST"])
def somar():
    dados_receba = request.get_json()
    try:
        numero1 = dados_receba['numero1']
        numero2 = dados_receba['numero2']
    except:
        return {"Message":"Erro"}, 400
    resultado = numero1 + numero2
    lista_calculos.append({
        'id': str(uuid.uuid4()),
        'numero1': numero1,
        'numero2': numero2,
        'resultado': resultado
    })
    return {"resultado": resultado}

@app.route("/calculos", methods=["GET"])
def calculos():
    return lista_calculos

@app.route("/deletar/<id>", methods=["DELETE"])
def metodo_delete(id):
    global lista_calculos
    lista_calculos = [d for d in lista_calculos if d.get('id') != id]

    return {}, 200

@app.route("/editar/<id>", methods=["PUT"])
def editar_item(id):
    global lista_calculos
    dados_receba = request.get_json()
    try:
        numero1 = dados_receba['numero1']
        numero2 = dados_receba['numero2']
    except:
        return {"Message":"Erro"}, 400

    lista_temp = []
    for calculo in lista_calculos:
        if calculo['id'] == id:
            resultado = numero1 = numero2
            lista_temp.append({
                'id': id,
                'numero1': numero1,
                'numero2': numero2,
                'resultado': resultado
            })
            return {}, 200
        else:
            return {}, 404

if __name__ == "__main__":
    app.run()