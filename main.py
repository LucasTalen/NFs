import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

def configuraNavegador():  
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    return requests.Session(), headers

def criarPlanilharComMinhasAcoes(valorIndicador):
    # Lista com os nomes dos indicadores
    nomeIndicador = ['Ativo','P/L', 'P/VP', 'DIVIDEND YIELD', 'PAYOUT', 'MARGEM LÍQUIDA', 'MARGEM BRUTA',
                     'MARGEM EBIT', 'MARGEM EBITDA ', 'EV/EBITDA', 'EV/EBIT', 'P/EBITDA', 'P/EBIT', 'P/ATIVO',
                     'P/CAP.GIRO', 'P/ATIVO CIRC LIQ', 'PSR', 'VPA', 'LPA', 'GIRO ATIVOS', 'ROE', 'ROIC',
                     'ROA', 'DÍVIDA LÍQUIDA / PATRIMÔNIO', 'DÍVIDA LÍQUIDA / EBITDA', 'DÍVIDA LÍQUIDA / EBIT',
                     'DÍVIDA BRUTA / PATRIMÔNIO', 'PATRIMÔNIO / ATIVOS', 'PASSIVOS / ATIVOS', 'LIQUIDEZ CORRENTE',
                     'CAGR RECEITAS 5 ANOS', 'CAGR LUCROS 5 ANOS']
    
    # Abre o arquivo CSV em modo de escrita e adiciona os valores dos indicadores como uma nova linha
    with open('minhas_acoes.csv', 'a', newline='') as arquivoCSV:
        escreverCSV = csv.writer(arquivoCSV)
        escreverCSV.writerow(valorIndicador)
        arquivoCSV.close()

        #escreverCSV.writerow(nomeIndicador) Titulo da tabela da planilha
 
def pesquisarAcoesDaBolsa(sesao, headers, ativo):
    # Constrói a URL da página que contém os indicadores da ação específica
    url = f"https://investidor10.com.br/acoes/{ativo}/"
    
    # Faz uma solicitação HTTP para obter o conteúdo da página
    conteudo = sesao.get(url, headers=headers)
    
    # Inicializa o objeto BeautifulSoup para analisar o conteúdo HTML
    pesquisador = BeautifulSoup(conteudo.text, "html.parser")
    
    # Encontra todas as divs com o id 'table-indicators' que contêm os indicadores
    indicadores = pesquisador.find_all('div', id='table-indicators')
    
    # Formata o texto dos indicadores removendo espaços e informações desnecessárias
    indicadorFormatado = indicadores[0].text.replace("\n\n\n\n\n", "\t").replace("\n", "")
    indicadorFormatado = indicadorFormatado.replace('Setor:', "").replace('Subsetor:', "").replace('Segmento:', "")
    
    # Divide o texto formatado em uma lista de indicadores separados por tabulação
    indicadorSeparado = indicadorFormatado.split("\t")
    
    # Cria uma nova lista para armazenar os indicadores formatados
    indicadoresFormatados = []
    indicadoresFormatados.extend(indicadorSeparado[::2])
    
    # Cria uma lista para armazenar os valores dos indicadores
    valorIndicador = []
    indicadoresDaAcao = {}
    valorIndicador.append(ativo)
    
    # Percorre os indicadores formatados e extrai a chave e o valor de cada indicador
    for item in indicadoresFormatados:
        chave, valor = item.rsplit(" ", 1)
        indicadoresDaAcao[chave] = valor
        valorIndicador.append(valor)
    
    # Chama uma função "criarPlanilharComMeusAtivos" passando os valores dos indicadores como argumento
    criarPlanilharComMinhasAcoes(valorIndicador=valorIndicador)

def pesquisarFiiDaBolsa(sesao, headers,ativo):
    # URL da página que contém os indicadores do FII
    url = f"https://investidor10.com.br/fiis/{ativo}/"
    
    # Faz uma solicitação HTTP para obter o conteúdo da página
    conteudo = sesao.get(url, headers=headers).text
    
    # Inicializa o objeto BeautifulSoup para analisar o conteúdo HTML
    pesquisador = BeautifulSoup(conteudo, "html.parser")
    
    # Encontra todas as seções com o id 'cards-ticker' que contêm os indicadores
    indicadores = pesquisador.find_all('section', id='cards-ticker')

    # Formata o texto dos indicadores removendo espaços e caracteres especiais
    texto_formatado = indicadores[0].text.replace("\n\n\n", "\t").replace("\n", "").replace("\t\t", "\n")
    texto_formatado = texto_formatado.replace("\t", "\n").replace(" ", "")
    
    # Divide o texto formatado em uma lista de indicadores
    lista_indicadores = texto_formatado.split("\n")
    
    # Remove o primeiro e último elemento da lista (cabeçalho e rodapé)
    indicadores_prontos = lista_indicadores[1:-1]
    
    # Cria uma nova lista para armazenar os indicadores formatados
    indicadores_formatados = []
    indicadores_formatados.extend(indicadores_prontos)
    
    # Exibe os indicadores formatados
    #print(indicadores_formatados)
    

    # Cria uma lista para armazenar os valores dos indicadores
    indicadoresDoFII = {}
    
    # Percorre os indicadores formatados e extrai a chave e o valor de cada indicador
    chave = indicadores_formatados[::2]
    valor = indicadores_formatados[1::2]

    indicadoresDoFII = dict(zip(chave,valor))
    valor.insert(0,ativo)

    # Chama uma função "criarPlanilharComMeusAtivos" passando os valores dos indicadores como argumento
    criarPlanilharComMeusFII(valorIndicador=valor)
    
def criarPlanilharComMeusFII(valorIndicador):
    # Lista com os nomes dos indicadores
    nomeIndicador = ['Ativo','Cotação','DY(12M)','P/VP','LiquidezDiária','VALORIZAÇÃO(12M)']
    
    # Abre o arquivo CSV em modo de escrita e adiciona os valores dos indicadores como uma nova linha
    with open('meus_fii.csv', 'a', newline='') as arquivoCSV:
        escreverCSV = csv.writer(arquivoCSV)
        escreverCSV.writerow(valorIndicador)
        arquivoCSV.close()

        #escreverCSV.writerow(nomeIndicador) Titulo da tabela da planilha
 
def meusAtivo(tipoDeAtivo):
    # Caminho do arquivo CSV contendo os dados dos ativos
    caminho_arquivo = "meusAtivos.csv"
   
    # Lê os dados do arquivo CSV e cria um DataFrame
    dados = pd.read_csv(caminho_arquivo, delimiter=';')
    df = pd.DataFrame(dados)
    
    if tipoDeAtivo == "acao":
        # Filtra os dados para obter apenas os ativos do tipo "Acao"
        filtroDeAcoes = df[df['tipo'] == 'Acao']
        
        # Obtém as colunas relevantes do DataFrame filtrado
        tipo = filtroDeAcoes['tipo']
        nome = filtroDeAcoes['nome']
        quantidade = filtroDeAcoes['quantidade']
        indice = filtroDeAcoes.index.to_list()
        
        # Retorna as colunas relevantes como resultados da função
        return tipo, nome, quantidade, indice
    elif tipoDeAtivo == 'FII':
        # Filtra os dados para obter apenas os ativos do tipo "FII"
        filtroDeFII = df[df['tipo'] == 'FII']
        
        # Obtém as colunas relevantes do DataFrame filtrado
        tipo = filtroDeFII['tipo']
        nome = filtroDeFII['nome']
        quantidade = filtroDeFII['quantidade']
        indice = filtroDeFII.index.to_list()
        
        # Retorna as colunas relevantes como resultados da função
        return tipo, nome, quantidade, indice

def iniciar():
    sesao,headers = configuraNavegador()
    tipo_FII,nome_FII,quantidade_FII,indice_FII = meusAtivo('FII')
    tipo_acoes,nome_acoes,quantidade_acoes,indice_acoes = meusAtivo('acao')
    
    for ativo in nome_FII:
        a = pesquisarFiiDaBolsa(sesao=sesao,headers=headers,ativo=ativo)
    for ativo in nome_acoes:
        a = pesquisarAcoesDaBolsa(sesao=sesao,headers=headers,ativo=ativo)
        
        
iniciar()
