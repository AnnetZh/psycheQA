from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
import datetime

from selenium.webdriver.common.action_chains import ActionChains

file = open("log.txt", 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()

radio_yes=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label')
radio_yes.click()
sleep(2)
radio_impressive=driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label')
radio_impressive.click()

file.close()