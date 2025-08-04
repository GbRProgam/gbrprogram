from playwright.sync_api import sync_playwright, Playwright
import time

cnpj = []

cnpj = int(input('Insira o CNPJ da Empresa: '))

#Entrar no site
with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://servicos.receitafederal.gov.br/servico/certidoes/#/home/cnpj/consultar/resultado")
    pagina.locator("div").filter(has_text="Pessoa Jurídica").get_by_role("option", name="Pessoa Jurídica").click() # Clicar em 'Pessoa Jurídica'
    pagina.get_by_role("textbox", name="CNPJ").fill(f'{cnpj}') # Colocar o CNPJ da empresa
    pagina.locator("div").filter(has_text="Consultar Certidão").get_by_role("button", name="Consultar Certidão").click()  # Clicar em Consultar Certidão
    pagina.locator("div").filter(has_text="Consultar Certidão").get_by_role("button", name="Consultar Certidão").click() # Clicar em Consultar Certidão
    with pagina.expect_download() as download_info:
        pagina.locator(".row-actions").first.click()
    download = download_info.value
    download.save_as("C:/Users/gasoferreira/Downloads/" + download.suggested_filename) #Faz o download do documento
    time.sleep(10)
    pagina.close()

            


    
   
    
    