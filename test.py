from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
link = ['https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230604387984000166650020005472501105350340|2|1|1|5304B1C5EF37ECBCB77C06D3E1EDDCC695AD2304','https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230623958283000184650010002466491109894252|2|1|1|9BCFB6C5919861911C500C5CFF59DE17CBFDF567']
compras = []
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
        valor = round(valor,2)
        compra = dict(loja = loja, preco =valor)
        compras.append(compra)
        
    
print(compras)
