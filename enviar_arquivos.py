
# Encontrar campo escolher arquivo
botao_escolher_arquivo = driver.find_element(By.XPATH, "//input[@id='myFile']")
sleep(1)
# Enviar caminho completo para o arquivo dentro do meu computador
botao_escolher_arquivo.send_keys(
    'D:\\Storage\\Desktop\\projetos selenium\\logo.jpg')
sleep(1)
# Clicar em enviar
botao_enviar = driver.find_element(
    By.XPATH, "//input[@value='Enviar Arquivo']")
sleep(1)
botao_enviar.click()
input('')
driver.close()