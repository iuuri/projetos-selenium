#localizar elemento
botao_dropdown = driver.find_element(By.ID, 'dropdownMenuButton')
#click pyton
botao_dropdown.click()
#click javascript
driver.execute_script('arguments[0].click()', botao_dropdown)