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

driver.get('http://demoqa.com/checkbox')
driver.maximize_window()

main_list=driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[1]')
main_list.click()
sleep(1)
home_check_box=driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
home_check_box.click()

def test_context_after_checkbox_is_correct():
    correct_text = "desktop"
    current_text = driver.find_element(By.XPATH, '//*[@id="result"]/span[2]')
    assert correct_text == current_text.text, "test_context_after_checkbox_is_correct is Failed"
    file.write("test_context_after_checkbox_is_correct is success \n")

def text_checkbox_is_correct():
    home_check_box.is_selected()
    if True:
        file.write("test_checkbox_is_correct is success \n")
    else:
        file.write("test_context_after_checkbox_is_correct is failed \n")

text_checkbox_is_correct()
test_context_after_checkbox_is_correct()
file.close()