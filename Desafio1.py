'''
Desafio 1
Encontre cada um deste botões usando o que aprendeu e descubra o estado de cada um desses botões
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(1)

botoes = driver.find_elements(By.XPATH, "//section[@class='jumbotron desafios1']//button")

for botao in botoes:
    if botao.is_enabled():
        print('Botão habilitado.')
    if botao.is_enabled() == False:
        print('Botão desabilitado')

input ('')