from selenium import webdriver
from selenium.webdriver.common.keys import Keys

botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
botao_windows.click()
botao_windows.send_keys(Keys.DOWN)
botao_windows.send_keys(Keys.TAB)
botao_windows.send_keys(Keys.PAGE_DOWN)