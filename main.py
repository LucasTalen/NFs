from flask import Flask, jsonify, Response
from flask_cors import CORS
from flask_socketio import SocketIO, emit

import requests
from bs4 import BeautifulSoup
import pandas as pd



#---------------------------------------
#você tem que herdar o meu código js no progama e puxar a função 
total = 0.0
def extrairDados(url):
    site = requests.get(url).text
    nome = BeautifulSoup(site, "html.parser")
    loja = nome.find("table").b.text
    soup = BeautifulSoup(site,"html.parser")
    for i in soup.find_all(id = "myTable"):
        a = i.get_text()
        a = a.replace("\n\n",'').replace("\t",'')
        b = []
        b = a.split("\n")
        b[-1] = b[-1].split()
        valor = float(b[-1][-1].replace(",","."))
        valor = round(valor,2)
        compra = dict(loja = loja, preco =valor)
        return jsonify(compra)     

#------------------------------------------





app = Flask(__name__)
CORS(app)
socketIO = SocketIO(app)


@socketIO.on('connect')
def criarConexao():
    emit('Conectado a API')



@app.route("/api")
def hello_world():
    resposta = extrairDados("https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230713574594030508650010005249781378283311|2|1|1|9CB061C0D016DBEDA8D27E6E20F4BA26025FF4A9")
    return Response(resposta, content_type='text/event-stream')

app.run(debug=True,port=80)