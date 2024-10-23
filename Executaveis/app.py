from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
import getpass
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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

driver, wait = iniciar_driver()
# Quais são os passos a fazer?

# 1 - Navegar até https://automatize.netlify.app/
driver.get('https://automatize.netlify.app')
sleep(2)
# Encontrar o elemento
campo_email = driver.find_element(By.ID, 'email')
sleep(2)
# 2 - Clicar no campo de e-mail
campo_email.click()
sleep(2)
# 3 - Digitar um e-mail
campo_email.send_keys('jhonatan@hotmail.com')
sleep(2)
# encontrar campo senha
campo_senha = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(2)
# 4 - Clicar no campo de senha
campo_senha.click()
sleep(2)
# 5 - Digitar uma senha
campo_senha.send_keys('123456')
sleep(2)
# 6 - Clicar no botão iniciar
botao_iniciar = driver.find_element(
    By.XPATH, "//button[@class='btn btn-primary']")
sleep(2)
botao_iniciar.click()
input()