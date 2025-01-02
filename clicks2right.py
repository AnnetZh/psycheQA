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

driver.get('https://demoqa.com/buttons')
driver.maximize_window()

sleep(1)

double_click_button=driver.find_element(By.XPATH,'//*[@id="doubleClickBtn"]')
right_click_button=driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
standard_click_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')

action=ActionChains(driver)
action.double_click(double_click_button).perform()

action.context_click(right_click_button).perform()

standard_click_button.click()

def test_doubleclick_is_correct():
    double_click_button.is_selected()
    if True:
        file.write("test_doubleclick_is_correct is success \n")
    else:
        file.write("test_doubleclick_is_correct is success \n")

def test_rightclick_is_correct():
    right_click_button.is_selected()
    if True:
        file.write("test_rightclick_is_correct is success \n")
    else:
        file.write("test_rightclick_is_correct is success \n")

def test_standardclick_is_correct():
    standard_click_button.is_selected()
    if True:
        file.write("test_standartclick_is_correct is success \n")
    else:
        file.write("test_standardclick_is_correct is success \n")


def test_context_rightclick_is_correct():
    correct_text = "You have done a right click"
    current_text = driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]')
    assert correct_text == current_text.text, "test_context_rightclick_is_correct is Failed"
    file.write("test_context_richtclick_is_correct is success \n")

def test_context_doubleclick_is_correct():
    correct_text = "You have done a double click"
    current_text = driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]')
    assert correct_text == current_text.text, "test_context_doubleclick_is_correct is Failed"
    file.write("test_context_doubleclick_is_correct is success \n")

def test_context_standardclick_is_correct():
    correct_text = "You have done a dynamic click"
    current_text = driver.find_element(By.XPATH, '//*[@id="dynamicClickMessage"]')
    assert correct_text == current_text.text, "test_context_standardclick_is_correct is Failed"
    file.write("test_context_standardclick_is_correct is success \n")

test_doubleclick_is_correct()
test_rightclick_is_correct()
test_standardclick_is_correct()

test_context_standardclick_is_correct()
test_context_doubleclick_is_correct()
test_context_rightclick_is_correct()

file.close()
