from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
import datetime
from datetime import timedelta

from selenium.webdriver.common.action_chains import ActionChains

file = open("log.txt", 'w')
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get('https://the-internet.herokuapp.com/horizontal_slider')
driver.maximize_window()

sleep(1)

slider=driver.find_element(By.XPATH, '//*[@id="content"]/div/div/input')
action=ActionChains(driver)
sleep(2)
action.click_and_hold(slider).move_by_offset(50, 0).release().perform()

file.close()