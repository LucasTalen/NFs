from main import verificarURL, get_tabela
from tabela import criar_planilha
from flask import Flask, jsonify, Response,request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/<token>/", methods=['GET'])
def montagem_da_tabela(token):
    url = request.args.get('url')
    
    print(url)
    print("-----------------------------")
    print(token)
    resposta = verificarURL(token,url)
    print(resposta)
    return resposta


@app.route("/api/<token>/baixar_tabela")
def baixar(token):
    tabela = get_tabela(token)
    criar_planilha(tabela)
    return send_file(r'C:\Users\Lucas\Documents\NFs\arquivo_para_download\planilha_Nfs.csv', as_attachment=True)

app.run(debug=True,port=80)