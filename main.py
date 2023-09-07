from flask import Flask, jsonify, request, render_template, redirect
import requests
from bs4 import BeautifulSoup
import pandas as pd

#---------------------------------------
#você tem que herdar o meu código js no progama e puxar a função 
link = ['https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230771385637001406650070001689639070627633|2|1|11|3.98|7936357977584f616b337a484b5359423132725969384158735a343d|1|680E5B22CA9E88F02A484802212C778AB215F274','https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230604387984000166650020005472501105350340|2|1|1|5304B1C5EF37ECBCB77C06D3E1EDDCC695AD2304','https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230623958283000184650010002466491109894252|2|1|1|9BCFB6C5919861911C500C5CFF59DE17CBFDF567']
total = 0.0
def extrairDados(total):
    tabela = {}
    tabela_nome = []
    tabela_valor = []
    for url in link:
        #url = f"https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230623958283000184650010002450161109877538|2|1|1|324E11E550C6E94284424B93527B2E440A18B80E"
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
            total += valor
            tabela_nome.append(loja)
            tabela_valor.append(valor)


        for j in tabela_nome:
            tabela['loja'] = tabela_nome

            tabela['valor'] = tabela_valor
    return tabela, total

#------------------------------------------

dados = extrairDados(total)




app = Flask(__name__)

@app.route("/api")
def hello_world():
    return f"<p>{dados}</p>"   

app.run(debug=True)