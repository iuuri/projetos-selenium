# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")

# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 1500);")

# Rolar X quantidade em pixels(subir)
driver.execute_script("window.scrollTo(0, -1500);")
