import requests
from bs4 import BeautifulSoup
import pandas as pd

tabela_usuario = {}
links = []
resposta = ''
total = 0.0








def get_tabela(token):
    return tabela_usuario[token]


def criarTabela(token,compra):
    try:
        if not tabela_usuario[token] == []:
            print("ok")
    except:
        tabela_usuario[token] = []    
    
    tabela_usuario[token].append(compra)
    print("Passou aqui no criarTabela")
    print(tabela_usuario)
    return criarTabelaHTML(tabela_usuario[token])


def criarTabelaHTML(tabela):
    print("Passou aqui no criarTabelaHTML")
    df = pd.DataFrame(tabela)
    tabela_html = df.to_html()
    print(tabela_html)

    print("------------Tabela Usuario-------------")
    print(tabela_usuario)
    print("------------Tabela Usuario-------------")



    return tabela_html
    


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
        compra = dict(loja = loja, preco = valor)
        return criarTabela(token,compra)



def verificarURL(token,url):    
    if "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=" in url:
        if not url in links:
            links.append(url)
            resposta = extrairDados(token,url)
        else:
            resposta = "link ja foi adicionado"
    else:
        resposta = "link errado"
    return resposta
        
