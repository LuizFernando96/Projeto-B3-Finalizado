import pandas as pd

# Seleciona o arquivo TXT (Selecionar de acordo com o local onde o arquivo se encontra)
f_bovespa = './cotaHIST_bruto/COTAHIST_A2023.TXT'

# Define o tamanho dos campos de acordo com o layout do arquivo da B3  
tamanho_campos=[2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,12,3]

# Lê como um "Fixed Width File" ou "Arquivo com Largura Fixa" e ignora a primeira linha com o 'header=0'
dados_acoes = pd.read_fwf(f_bovespa, widths=tamanho_campos, header=0)

# Nomea as colunas de acordo com o layout do arquivo da B3
dados_acoes.columns = [    
"tipo_registro",
"data_pregao",
"cod_bdi",
"cod_negociacao",
"tipo_mercado",
"nome_empresa",
"especificacao_papel",
"prazo_dias_merc_termo",
"moeda_referencia",
"preco_abertura",
"preco_maximo",
"preco_minimo",
"preco_medio",
"preco_ultimo_negocio",
"preco_melhor_oferta_compra",
"preco_melhor_oferta_venda",
"numero_negocios",
"quantidade_papeis_negociados",
"volume_total_negociado",
"preco_exercicio",
"indicador_correcao_precos",
"data_vencimento",
"fator_cotacao",
"preco_exercicio_pontos",
"codigo_isin",
"num_distribuicao_papel"]

# Elimina a ultima linha do arquivo (o Trailer segundo o layout do arquivo da b3)
linha=len(dados_acoes["data_pregao"])
dados_acoes=dados_acoes.drop(linha-1)

# Ajusta valores com vírgula (dividir os valores dessas colunas por 100)
listaVirgula=[
"preco_abertura",
"preco_maximo",
"preco_minimo",
"preco_medio",
"preco_ultimo_negocio",
"preco_melhor_oferta_compra",
"preco_melhor_oferta_venda",
"volume_total_negociado",
"preco_exercicio",
"preco_exercicio_pontos"
]

for coluna in listaVirgula:
    dados_acoes[coluna]=[i/100. for i in dados_acoes[coluna]]

# Altera o formato da data de 'AAAAMMDD' para 'DDMMAAAA'
dados_acoes['data_pregao'] = pd.to_datetime(dados_acoes.data_pregao)
dados_acoes['data_pregao'] = dados_acoes['data_pregao'].dt.strftime('%d/%m/%Y')

ls_empresas = [
    "CSAN3", "CMIG4", "VIIA3", "BRAP4", "RENT3", "TAEE11", "WEGE3", "CMIN3", "SLCE3"
]
dados_filtrados = dados_acoes[dados_acoes['cod_negociacao'].isin(ls_empresas)]

print(dados_filtrados)

# Salva o arquivo no formato csv ---> Pode nomear o arquivo como quiser, no meu exemplo nomeei de "COSAN2023.csv"
fileO = open('COTAHIST_A2023.csv', "w")
fileO.write(dados_filtrados.to_csv())
fileO.close

    