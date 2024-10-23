
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


login = ('Digite seu email: ')
senha = getpass.getpass('Digite sua senha: ')

driver, wait = iniciar_driver()

#Entrar no site do instagram
driver.get('https://www.instagram.com')
sleep(1)

# Clicar e digitar meu usuário
campo_usuario = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, "//input[@name = 'username']")))
campo_usuario.send_keys(login)
sleep(3)

# Clicar e digitar minha senha 
campo_senha = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, "//input[@name = 'password']")))
campo_senha.send_keys(senha)
sleep(3)

# Clicar no campo entrar
btn_entrar = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, "//button[@type = 'submit']")))
btn_entrar.click()
sleep(3)

# Navegar até a página alvo
driver.get('https://www.instagram.com/_iuuris/?next=%2F')
sleep(5)

# Clicar na última  postagem
postagens = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.CLASS_NAME, "_aagu")))
sleep(2)
postagens[0].click()
sleep(5)

# Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
elementos_postagens = wait.until(CondicaoExperada.visibility_of_any_elements_located(By.XPATH,"//div[@class ='x6s0dn4 x78zum5 xdt5ytf xl56j7k']"))

if len(elementos_postagens) == 7:
    elementos_postagens[3].click()
else:
    print('Postagem ja foi curtida')




