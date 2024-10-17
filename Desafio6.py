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
driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(1)
driver.execute_script("window.scrollTo(0, 2300);")
sleep(1)


dropdown = driver.find_element(By.XPATH, "//select[@id = 'paisesselect']")
opcoes = Select(dropdown)

opcoes.select_by_value('estadosunidos')
sleep(1)

opcoes.select_by_value('africa')
sleep(1)

opcoes.select_by_value('chille')
sleep(1)

input('')