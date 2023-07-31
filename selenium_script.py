import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox import options
from selenium import webdriver

from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())
username = getenv("USERNAME_LOGIN")
password = getenv("PASSWORD_LOGIN")


options = Options()
options.headless = True 

navegador = webdriver.Firefox(options=options)

link = "https://ava.ampli.com.br/login"

navegador.get(url=link)

time.sleep(5)
navegador.find_element(by=By.ID, value='input-field-cpfLogin').send_keys(username)
time.sleep(5)

try:
    navegador.find_element(by=By.XPATH, value='/html/body/cookie-police-bar/div/div[2]/button').click()
except Exception as e:
    pass # the cookie police bar doesn't always shows off


time.sleep(5)
navegador.find_element(by=By.ID, value='btnForward').click()
time.sleep(5)
navegador.find_element(by=By.ID, value='inputPassword').send_keys(password)
time.sleep(5)
navegador.find_element(by=By.ID, value='btnForward').click()
time.sleep(5)

try:
    navegador.find_element(by=By.XPATH, value='/html/body/cookie-police-bar/div/div[2]/button').click()
except Exception as e:
    pass

time.sleep(5)
navegador.find_element(by=By.ID, value='card-enter-course-bacharelado-0').click()
time.sleep(5)
navegador.find_element(by=By.ID, value='internalCard-active-carousel-actives-0').click()
time.sleep(5)

subject_title = navegador.find_element(by=By.ID, value='subject-title').text
time.sleep(2)

exam_date = navegador.find_element(by=By.ID, value='period-exam-date').text

exam_date = exam_date.split(" ")[2]

exam_date = datetime.strptime(exam_date, '%m/%d/%Y')

current_date = datetime.now()

time_difference = exam_date - current_date

time_difference = str(time_difference).split(",")

async def generate_exam_alert() -> str:
    message =  f"Faltam {time_difference[0].replace('days', 'dias')} e{time_difference[1].split(':')[0]} horas para sua prova de {subject_title}."

    navegador.quit()

    return message
