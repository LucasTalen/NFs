from flask import Flask, jsonify, Response,request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import pandas as pd



#---------------------------------------
#você tem que herdar o meu código js no progama e puxar a função 
tabela = []
links = []
resposta = ''
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
        tabela.append(compra)
        #------------
        df = pd.DataFrame(tabela)
        tabela_html = df.to_html()
        print(tabela_html)
        return tabela_html 
    #jsonify(compra)     

#------------------------------------------
def verificarURL(url):    
    if "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=" in url:
        if not url in links:
            links.append(url)
            resposta = extrairDados(url)
            print(type(resposta))
            print("------------------------")
        else:
            print("link ja foi adicionado")
            resposta = "link ja foi adicionado"
    else:
        resposta = "link errado"
        print("link errado")
    return resposta
        
    


app = Flask(__name__)
CORS(app)


@app.route("/api", methods=['GET'])
def hello_world():
    url = request.args.get('url')
    print(url)
    resposta = verificarURL(url)
    print(resposta)
    return resposta
    

app.run(debug=True,port=80)