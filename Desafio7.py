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
sleep(2)

#Salvar janela inicial
janela_inicial = driver.current_window_handle

#Encontrar o desafio 7 
driver.execute_script("window.scrollTo(0, 2500);")

#Abrir uma nova janela 
btn_abrir_nova_janela = driver.find_element(By.XPATH, "//button[text() = 'Abrir nova janela']")
btn_abrir_nova_janela.click()

#Mudar para nova janela 
janelas = driver.window_handles

for janela in janelas:
    if janela not in janela_inicial:
        #Alterar para a nova janela 
        driver.switch_to.window(janela)
        sleep(2)
        campo_pesquisa = driver.find_element(By.ID, "opiniao_sobre_curso")
        campo_pesquisa.send_keys("Muito bom!Estou aprendendo bastante.")
        sleep(2)

        btn_pesquisar = driver.find_element(By.ID, "fazer_pesquisa")
        btn_pesquisar.click()
        sleep(2)

        driver.close()

#Voltar para janela inicial
driver.switch_to.window(janela_inicial)

#Digitar algo 
campo_desafio7 = driver.find_element(By.ID, 'campo_desafio7')
campo_desafio7.send_keys('Digitar alguma coisa')




input('')