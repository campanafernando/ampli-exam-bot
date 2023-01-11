import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import options
from selenium import webdriver

options = Options()
options.headless = False  # permite que a operaÃ§ao seja feita com o navegador fechado

navegador = webdriver.Firefox(options=options)

link = "https://ava.ampli.com.br/login" # link do site onde os dados serao coletados

navegador.get(url=link)

time.sleep(5)
navegador.find_element(by=By.ID, value='cpfLogin').send_keys('')
time.sleep(5)
navegador.find_element(by=By.CLASS_NAME, value='_hj-kWRoL__styles__openStateToggle').click()
time.sleep(5)
navegador.find_element(by=By.ID, value='btnFoward').click()
time.sleep(5)
navegador.find_element(by=By.ID, value='inputPassword').send_keys('')
time.sleep(5)
navegador.find_element(by=By.ID, value='btnFoward').click()
time.sleep(5)
navegador.find_element(by=By.XPATH, value='/html/body/cookie-police-bar/div/div[2]/button').click()
time.sleep(5)
navegador.find_element(by=By.ID, value='enterCourse-Engenharia-de-Software').click()
time.sleep(5)
navegador.find_element(by=By.XPATH, value='//*[@id="titleSubject-carousel-actives-1"]').click()
time.sleep(5)

