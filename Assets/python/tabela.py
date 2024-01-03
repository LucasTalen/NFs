import csv
import pandas as pd

def criar_planilha(tabela):
    df = pd.DataFrame(tabela,columns=['loja','preco'])
    total = df['preco'].sum()
    df.loc[len(df)] = ['Total', total]

    print(df)
    df.to_csv('./arquivo_para_download/planilha_Nfs.csv',index=False)   


tabela = [['Es',12],['mg',123],['RJ',1]]



criar_planilha(tabela)
