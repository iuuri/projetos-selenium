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

email = 'Digitar email'
senha = 'Digitar senha'

# ir até o facebook
driver.get('https://www.facebook.com/')
sleep(5)
# Digitar email
campo_email = driver.find_element(By.ID, 'email')
sleep(5)
campo_email.send_keys(email)
sleep(5)
# Digitar senha
campo_senha = driver.find_element(By.ID, 'pass')
sleep(5)
campo_senha.send_keys(senha)
sleep(5)
# clicar em login
botao_entrar = driver.find_element(By.XPATH, "//button[@name='login']")
sleep(5)
botao_entrar.click()
sleep(5)
# encontrar e clicar no campo de postagem
campo_status = driver.find_element(By.XPATH,"//div[@class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']")
sleep(2)
campo_status.click()
sleep(5)
# Clicar dentro do campo de status
dentro_campo_status = driver.find_element(By.XPATH,"//p[@class='i1ao9s8h hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5']")
sleep(1)
dentro_campo_status.click()
sleep(1)
# Digitar algo
dentro_campo_status.send_keys('Olá, boa tarde a todos!')
sleep(3)
# Clicar em publicar
botao_publicar = driver.find_element(By.XPATH,"//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu tv7at329']")
sleep(2)
botao_publicar.click()

input('')