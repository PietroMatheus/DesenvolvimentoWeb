from flask import Flask, request
import uuid
import psycopg

app = Flask(__name__)
connection_db = psycopg.connect("dbname=turma3f user=postgres password=3f@db host=164.90.152.205 port=80")

@app.route("/pessoas", methods=["POST"])
def incluir_pessoa():
    dados_recebidos = request.get_json()
    id = uuid.uuid4()
    nome = dados_recebidos["nome"]

    cursor = connection_db.cursor()
    cursor.execute(
        "INSERT INTO pessoas (id, nome) VALUES (%s, %s)",
        (id, nome)
    )
    connection_db.commit()


    return {
        'id': id
    }

@app.route("/pessoas", methods=["GET"])
def get_pessoas():
    cursor = connection_db.cursor()
    cursor.execute("select id, nome from pessoas order by nome")

    lista = []
    for item in cursor:
        lista.append({
            'id': item[0],
            'nome': item[1]
        })
        
    return lista

@app.route("/pessoas/<id>", methods=["PUT"])
def atualizar_pessoas(id):
    dados_recebidos = request.get_json()
    nome = dados_recebidos["nome"]

    cursor = connection_db.cursor()
    cursor.execute(
        "UPDATE pessoas SET nome = %s WHERE id = %s",
        (nome, id)
    )
    connection_db.commit()

    return {
        'id': id,
        'nome': nome
    }