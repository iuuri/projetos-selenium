from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,700', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
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

#Acessar site
driver.get('https://cursoautomacao.netlify.app/')

# #Localizar elemento por id 
# btn_alerta = driver.find_element(By.ID, 'buttonalerta')

# if btn_alerta is not None:
#     print('Botão encontrado.')

# #Localizar elemento por CLASS NAME
# logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
# nav = driver.find_element(By.CLASS_NAME, 'nav-link')

# if logo is not None:
#     print('Logo encontrado.')
# if nav is not None:
#     print('Navegação encontrada')

# #Localizar elemento por NAME
# campo_nome = driver.find_element(By.NAME, 'seu-nome')
# radio_btn = driver.find_elements(By.NAME,'exampleRadios')

# if campo_nome is not None:
#     print('Botão seu nome encontrado.')
# if radio_btn is not None:
#     print('Encontramos os radios buttons')

# #Localizar elemento por TEXTO em LINKS
# link_home = driver.find_element(By.LINK_TEXT, 'Home')
# link_parcial = driver.find_element(By.PARTIAL_LINK_TEXT,'Des')

# if link_home is not None:
#     print('Link home encontrado.')
# if link_parcial is not None:
#     print('Link parcial encontrado')

# #Localizar elemento por TEXTO
# texto = driver.find_element(By.XPATH, "//*[text()='ZONA DE TESTES']")

# if texto is not None:
#     print(texto.text)

# # #Localizar elemento por TAG
# tag_titulo = driver.find_element(By.TAG_NAME, 'h1')
# tag_titulos = driver.find_elements(By.TAG_NAME, 'h4')

# if tag_titulos is not None:
#     print(tag_titulo.text) 





input('aperta uma tecla para fechar')

