import pandas as pd

# Seleciona o arquivo JSON (Selecionar de acordo com o local onde o arquivo se encontra)
dados_acao = pd.read_json('./BRUTO/UGPA3.json')

# Adiciona a coluna 'codigoNegocio' no DataFrame
df = pd.DataFrame(dados_acao)

#df['lucroLiquido'] = df['lucroLiquido'].astype(int)
df['cod_negociacoes'] = ['UGPA3']*20

df['year'] = df.apply(lambda row: pd.Timestamp(f'{row["year"]}-{3*(row["quarter"]-1)+1}-01'), axis=1)
df['year'] = df['year'].dt.strftime('%d/%m/%Y')

# Define quais colunas serão mostradas
dr = df[['cod_negociacoes','year', 'quarter', 'lucroLiquido']]

#Salva o arquivo no formato csv
fileO = open('UGPA3_lucro.csv', "w")
fileO.write(dr.to_csv())
fileO.close