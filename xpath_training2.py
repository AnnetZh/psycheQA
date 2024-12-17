from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file=open("log.txt",'w')
driver=webdriver.Chrome()
def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name=driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login='problem_user'
    user_name.send_keys(login)
    file.write("Successful login \n")

    passw=driver.find_element(By.XPATH,'//input[@id="password"]')
    password='secret_sauce'
    passw.send_keys(password)
    file.write("Successful password \n")

    login_button=driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()
    file.write("Successful click login \n")

set_up()
login()
file.close()
sleep(3)

#//input[@placeholder="Please enter your Message"]
#//placeholder[contains(text(),"Please enter your Message")]
#//input[@placeholder='Please enter your Message']
#//*[@id="box"]
#//div[@class="mr-10"][3]
#//*[@id="example_wrapper"]/div[1]/a[1]