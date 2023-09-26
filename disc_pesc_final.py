# importações
import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    navegador = p.chromium.launch(headless = False) # headless = abre a janela do navegador
    pagina = navegador.new_page()

    # acessa a page
    pagina.goto("https://cos.ufrj.br/index.php/pt-BR/pos-graduacao/disciplinas-3")
    url = pagina.locator('//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a').get_attribute('href')
    nome_arq = pagina.locator('//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a').text_content().strip().replace('/','_') + '.xlsx'
    url = 'https://cos.ufrj.br' + url
    print(nome_arq)

    # fecha o navegador
    navegador.close()
# TERMINA DE USAR O PLAYWRIGHT

#INÍCIO BEAUTIFULSOUP
requisicao = requests.get(url)
# print(requisicao)         # caso o valor seja 200, deu certo a requisição
# print(requisicao.text)    # printa o html do site sem mostrar a forma como está estruturado 

# PRINTA O HTML ESTRUTURADO
site = BeautifulSoup(requisicao.text, 'html.parser')

# LIMPANDO OS DADOS DO SITE
tabela = site.findAll('tr')     # acha as linhas
linhas = []     
for linha in tabela:
    linhas.append(linha.text.split('\n')[1:-2])     # faz a formatação da tabela para conseguir manusear com facilidade

# VARIÁVEIS AUXILIARES
dataframe = {}      # dataframe para exportação para csv ou excel
lista = []          # lista para auxiliar na criação do dataframe

# CRIAÇÃO DO DATAFRAME
for c in range(0, len(linhas[0])):          # anda nas colunas da tabela
    for l in range(1, len(linhas)):         # anda nas linhas da tabela (começa no índice 1 pois o índice 0 é o header)
        lista.append(linhas[l][c])          # adiciona o item da coluna de cada linha
    dataframe[linhas[0][c]] = list(lista)   # adiciona no dicionário a lista de itens de cada coluna
    lista.clear()

# EXPORTANDO PARA CSV OU EXCEL
disc_df = pd.DataFrame.from_dict(dataframe)
disc_df.to_excel(nome_arq)
print('Arquivo Criado!!')