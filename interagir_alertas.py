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
sleep(2)

#Botão Alerta 
btn_alerta = driver.find_element(By.ID, 'buttonalerta')
btn_alerta.click()
sleep(2)

#Mudar para caixa de alerta
alerta1 = driver.switch_to.alert
alerta1.accept()
sleep(2)

#Botão confirmar 
btn_confirmar = driver.find_element(By.ID, 'buttonconfirmar')
btn_confirmar.click()
sleep(2)

#Mudar para caixa de alerta e aceitar 
alerta2 = driver.switch_to.alert
alerta2.accept()
sleep(2)

#Botão confirmar (cancelar)
btn_confirmar = driver.find_element(By.ID, 'buttonconfirmar')
btn_confirmar.click()
sleep(2)

#Mudar para caixa de alerta e cancelar 
alerta2 = driver.switch_to.alert
alerta2.dismiss()
sleep(2)

#Botão prompt 
btn_prompt = driver.find_element(By.ID, 'botaoPrompt')
btn_prompt.click()
sleep(2)

#Digitar no prompt 
alerta3 = driver.switch_to.alert
alerta3.send_keys('22/10')
alerta3.accept()
sleep(1)
alerta3.accept()



input('')