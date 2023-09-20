import requests
from bs4 import BeautifulSoup
import pandas as pd

tabela_usuario = {}
tabela = []
links = []
resposta = ''
total = 0.0

def extrairDados(token, url):
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
        tabela_usuario[token] = tabela
        df = pd.DataFrame(tabela_usuario[token])
        tabela_html = df.to_html()
        return tabela_html 
   

def verificarURL(url):    
    if "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=" in url:
        if not url in links:
            links.append(url)
            resposta = extrairDados(url)
        else:
            resposta = "link ja foi adicionado"
    else:
        resposta = "link errado"
    return resposta
        
    




