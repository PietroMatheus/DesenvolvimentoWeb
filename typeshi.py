from flask import Flask, request 

app = Flask(__name__)

lista_calculos = []

@app.route("/soma", methods=["POST"])
def somar():
    dados_receba = request.get_json()
    numero1 = dados_receba['numero1']
    numero2 = dados_receba['numero2']
    resultado = numero1 + numero2
    lista_calculos.append({
        'numero1': numero1,
        'numero2': numero2,
        'resultado': resultado
    })
    return {"resultado": resultado}

@app.route("/calculos", methods=["GET"])
def calculos():
    return lista_calculos

# @app.route("/", methods=["PUT"])
# def metodo_put():
#     dados_receba = request.get_json()
#     coisalegal.append({"nome": dados_receba["nome"]})
#     return {"message": "deu boa"}

# @app.route("/", methods=["DELETE"])
# def metodo_delete():
#     dados_deletar = request.get_json()
#     coisalegal.remove({"nome": dados_deletar["nome"]})
#     return {"message": "deu boa"}