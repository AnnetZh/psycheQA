from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
import datetime
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

file = open("log.txt", 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = 'standard_user'
    user_name.send_keys(login)
    file.write("Successful login \n")

    passw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = 'secret_sauce'
    passw.send_keys(password)
    file.write("Successful password \n")

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()
    file.write("Successful click login \n")

set_up()
sleep(2)
login()

select=Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
sleep(2)

select.select_by_visible_text('Price (low to high)')

file.close()