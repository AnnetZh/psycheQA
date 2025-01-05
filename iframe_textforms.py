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

driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')
driver.maximize_window()

sleep(1)

iframe=driver.find_element(By.XPATH,'//*[@id="iFrame1"]')
driver.switch_to.frame(iframe)
lon=driver.find_element(By.XPATH,'/html/body/div/div/div[2]')
sleep(2)
lon.send_keys(Keys.CONTROL+'a')
lon.send_keys(Keys.DELETE)
italic_button_iframe=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/button[2]')
italic_button_iframe.click()
lon.send_keys("Your message")


file.close()