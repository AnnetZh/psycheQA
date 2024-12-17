from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
driver.maximize_window()

user_name=driver.find_element(By.XPATH,'//input[@id="user-name"]')
passw=driver.find_element(By.XPATH,'//*[@id="password"]')
# //div[@class="form_group"][1]
# //h4[contains(text(),"Password for all users:")]
login='problem_user'
user_name.send_keys(login)
password='secret_sauce'
passw.send_keys(password)


sleep(6)

#//input[@placeholder="Please enter your Message"]
#//placeholder[contains(text(),"Please enter your Message")]
#//input[@placeholder='Please enter your Message']
#//*[@id="box"]
#//div[@class="mr-10"][3]
#//*[@id="example_wrapper"]/div[1]/a[1]