import pandas as pd

# Seleciona o arquivo JSON (Selecionar de acordo com o local onde o arquivo se encontra)
dados_acao = pd.read_json('./receitaLiquida_bruto/getrevenueCSAN3.json')

# Ajusta o valor (divide o valor por 1000)
dadosVirgula=[
"lucroLiquido"    
]

for coluna in dadosVirgula:
    dados_acao[coluna]=[i/1000 for i in dados_acao[coluna]]

# Adiciona a coluna 'codigoNegocio' no DataFrame
df = pd.DataFrame(dados_acao)
df['codigoNegocio'] = ['CSAN3']*20

df['year'] = df.apply(lambda row: pd.Timestamp(f'{row["year"]}-{3*(row["quarter"]-1)+1}-01'), axis=1)
df['year'] = df['year'].dt.strftime('%d/%m/%Y')

# Define quais colunas serão mostradas
dr = df[['codigoNegocio','year', 'quarter', 'lucroLiquido']]