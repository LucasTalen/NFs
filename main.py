from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd

#---------------------------------------
#você tem que herdar o meu código js no progama e puxar a função 
total = 0.0
def extrairDados(total,url):
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

@app.route("/api")
def hello_world():
    resposta = extrairDados(total,url)
    return resposta

app.run(debug=True)