from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys

file=open("log.txt",'w')
driver=webdriver.Chrome()
option=webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver=webdriver.Chrome(options=option)

#Scenario functions---
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


def login_with_enter():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = 'problem_user'
    user_name.send_keys(login)
    file.write("Successful login \n")

    passw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = 'secret_sauce'
    passw.send_keys(password)
    file.write("Successful password \n")

    passw.send_keys(Keys.ENTER)
    file.write("Successful click login \n")

def fake_login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = 'problem_user'
    user_name.send_keys(login)
    file.write("Successful login \n")

    passw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = 'secret_sauce11'
    passw.send_keys(password)
    file.write("Successful fake password \n")

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()
    file.write("Successful click login \n")

#def refresh_page():
  #  driver.refresh()

# End of Scenario functions

# Tests ----

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

def test_fake_login_label():
    correct_text="Epic sadface: Username and password do not match any user in this service"
    current_text=driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text==current_text.text, 'test_fake_login_label is Failed'
    file.write("test_fake_login_label is successful \n")
#End of tests

def sc_real_login():
    set_up()
    login()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_with_enter():
    set_up()
    login_with_enter()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
#    sleep(2)
#    refresh_page()

    test_fake_login_label()

set_up()
user_name=driver.find_element(By.XPATH,'//input[@id="user-name"]')
login='problem_user'
user_name.send_keys(login)
sleep(2)
#user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(Keys.CONTROL+"a")

#sc_fake_login()
#sc_real_login_with_enter()
file.close()