from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

file=open("log.txt",'w')
driver=webdriver.Chrome()
option=webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver=webdriver.Chrome(options=option)

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

def test_login_redirect():
    correct_url='https://www.saucedemo.com/inventory.html'
    get_url=driver.current_url

    assert correct_url == get_url,"test_login_redirect is Failed"
    file.write("test_login_redirect is success \n")

def test_context_after_login_is_correct():
    correct_text="Products"
    current_text=driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text==current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is success \n")
set_up()
login()

test_login_redirect()
test_context_after_login_is_correct()

file.close()