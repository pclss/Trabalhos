# importa biblioteca playwright
from playwright.sync_api import sync_playwright

# abre o navegador playwright
with sync_playwright() as p:
    navegador = p.chromium.launch(headless = False) # headless = abre a janela do navegador
    pagina = navegador.new_page()
    
    # acessa a page
    pagina.goto("https://www.imdb.com")
    pagina.mouse.wheel(0, 2000)     # "scroll" do mouse

    # força espera para a página carregar
    # pagina.wait_for_timeout(20000)

    # listas para guardar os nomes dos filmes
    top_10_250 = []     # top 10 dos 250 melhores filmes
    top_10_sem = []     # top 10 melhores filmes da semana
    
    # Pega a classificação
    print(pagina.locator(
        'xpath=//*[@id="__next"]/main/div/div[3]/div[3]/section[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/span').text_content())

    # seleciona o top 10 semanal
    for i in range(1, 11):
        top_10_sem.append(pagina.locator(
            f'xpath=//*[@id="__next"]/main/div/div[3]/div[3]/section[2]/div/div[2]/div/div/div[2]/div[{i}]/a/span').text_content())

    # muda a page
    pagina.goto("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

    # seleciona os nomes dos 10 melhores filmes
    for i in range(1, 11):
        top_10_250.append(pagina.locator(
            f'xpath=/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3').text_content())
    
    # print do top 10 filmes
    print('Top 10 dos 250 melhores filmes ===================================================================')
    print(*top_10_250, sep='\n', end = '\n\n')

    # print do top 10 semanal
    print('Top 10 Semanal ===================================================================================')
    print(*top_10_sem, sep='\n')

    # fecha o navegador
    navegador.close()