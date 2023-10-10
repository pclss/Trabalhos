import pandas as pd
from playwright.sync_api import sync_playwright

########## ABRE PLAYWRIGHT ##########
with sync_playwright() as p:
    navegador = p.chromium.launch(headless = False) # headless = abre a janela do navegador
    pagina = navegador.new_page()

    # acessa a page
    pagina.goto("https://cos.ufrj.br/index.php/pt-BR/pos-graduacao/disciplinas-3")

    # COPIA O LINK DO OBJETO
    url = pagina.locator('//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a').get_attribute('href')
    
    # DEFINE O NOME DO ARQUIVO
    nome_arq = pagina.locator('//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a').text_content().strip().replace(
        '/','_') + '.xlsx'
    
    # ADICIONA A PARTE INICIAL DA URL
    url = 'https://cos.ufrj.br' + url
    print(nome_arq)

    # fecha o navegador
    navegador.close()
########## FIM PLAYWRIGHT ##########

########## LEITURA DE TABELA HTML ##########
url = pd.read_html(url)
url = pd.DataFrame(url[0]) # transforma em um dataframe
url.to_excel(nome_arq) # salva a o dataframe em um arquivo excel