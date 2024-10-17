from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,600', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)
        chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'C:\\Users\\iuri.santos\\Desktop\\Projetos\\Curso\\projetos-selenium',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
        
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver
driver = iniciar_driver()
# navegar até o site
driver.get('https://cursoautomacao.netlify.app')
sleep(1)

paises_dropdown = driver.find_element(By.XPATH, "//select[@id = 'paisselect']")
opcoes = Select(paises_dropdown)
sleep(1)

#Selecionar por indice 
opcoes.select_by_index(2)
sleep(1)

#Selecionar por value
opcoes.select_by_value('estadosunidos')
sleep(1)

#Selecionar por texto em exibição
opcoes.select_by_visible_text('Brasil')
sleep(1)

input('')
