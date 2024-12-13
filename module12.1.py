from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
driver.maximize_window()

user_name=driver.find_element(By.ID,'user-name')
passw=driver.find_element(By.ID,'password')
login='problem_user'
user_name.send_keys(login)
password='secret_sauce'
passw.send_keys(password)


sleep(6)