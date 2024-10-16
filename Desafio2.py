# Desafios 2

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

nome = 'Iuri Souza'

campo_nome = driver.find_element(By.ID,'dadosusuario')
campo_nome.send_keys(nome)

btn_enviar = driver.find_element(By.ID,'desafio2')
btn_enviar.click()

validar_nome = driver.find_element(By.ID,'escondido')
validar_nome.send_keys(nome)

btn_validar = driver.find_element(By.ID,'validarDesafio2')
btn_validar.click()

input('')