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

driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

sleep(1)

#date_input=driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
date_input=driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')
date_input.send_keys(Keys.CONTROL+'a')
date_input.send_keys(Keys.DELETE)

sleep(2)

#current_date=datetime.datetime.now().strftime('%m.%d.%Y')

current_date=datetime.datetime.now()

new_date=current_date+timedelta(days=10)
date_input.send_keys(new_date.strftime('%m.%d.%Y'))


file.close()