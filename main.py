from selenium import webdriver
from selenium.webdriver.common.by import By

a=input('digite algo: ')
print('{}'.format(a))

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(a)
navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()