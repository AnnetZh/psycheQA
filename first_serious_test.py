from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys
import datetime

from selenium.webdriver.common.action_chains import ActionChains

#cоздаем файл, который будет выводить нам проделанные пункты в случае успеха.

file = open("log.txt", 'w')
driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

#запускаем сайт
def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

#логинимся
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

#проверки перехода и содержания страницы
def test_login_redirect():
    correct_url = 'https://www.saucedemo.com/inventory.html'
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is success \n")

def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is success \n")

#обобщаем вход
def sc_login():
        login()
        test_login_redirect()
        test_context_after_login_is_correct()

#добавляем товары в корзину
def add_backpack_to_cart():
    add_backpack=driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_backpack.click()
    file.write("Sauce Labs Backpack successfully added \n")
    #add_backpack=29.99

def add_fleece_jacket_to_cart():
    add_jacket=driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    add_jacket.click()
    file.write("Sauce Labs Fleece Jacket successfully added\n")
    #add_jacket=49.99

#заходим в корзину
def go_to_cart():
    cart=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    cart.click()
    file.write("Cart is successfully opened\n")

#проверка перехода и содержания страницы корзины и скриншот товаров в корзине
def test_cart_redirect():
    correct_url='https://www.saucedemo.com/cart.html'
    get_url = driver.current_url

    assert correct_url == get_url, "test_cart_redirect is Failed"
    file.write("test_cart_redirect is success \n")

def test_context_cart_is_correct():
    correct_text = "Your Cart"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    driver.save_screenshot(f"first_serious_test\\screenshot_test_context_cart_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")
    assert correct_text == current_text.text, "test_context_cart_is_correct is Failed"
    file.write("test_context_cart_is_correct is success \n")

#обобщаем корзину

def sc_cart():
    add_backpack_to_cart()
    add_fleece_jacket_to_cart()
    go_to_cart()
    test_cart_redirect()
    test_context_cart_is_correct()

#идем в чекаут
def checkout_step_one():
    checkout_button=driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout_button.click()
    file.write("Successful checkout\n")

#проверки перехода и содержания страницы чекаута
def test_checkout_step_one_redirect():
    correct_url='https://www.saucedemo.com/checkout-step-one.html'
    get_url = driver.current_url

    assert correct_url == get_url, "test_checkout_step_one_redirect is Failed"
    file.write("test_checkout_step_one_redirect is success \n")

def test_context_checkout_step_one_is_correct():
    correct_text = "Checkout: Your Information"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    assert correct_text == current_text.text, "test_context_checkout_step_one_is_correct is Failed"
    file.write("test_context_checkout_step_one_is_correct is success \n")

#вбиваем данные и переходим к оформлению заказа
def checkout_inside():
    first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    name = 'Anna'
    first_name.send_keys(name)
    file.write("Successful first name \n")

    last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    surname = 'Ivanova'
    last_name.send_keys(surname)
    file.write("Successful surname \n")

    postal_code=driver.find_element(By.XPATH,'//input[@id="postal-code"]')
    zip=123456
    postal_code.send_keys(zip)
    file.write("Successful postal code\n")

    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    file.write("Successful click continue-button \n")

#проверяем переход и содержание после кнопки чекаут

def test_checkout_step_two_redirect():
    correct_url = 'https://www.saucedemo.com/checkout-step-two.html'
    get_url = driver.current_url

    assert correct_url == get_url, "test_checkout_step_two_redirect is Failed"
    file.write("test_checkout_step_two_redirect is success \n")


def test_checkout_step_two_is_correct():
    correct_text = "Checkout: Overview"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    driver.save_screenshot(f"first_serious_test\\screenshot_test_context_checkout2_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")
    assert correct_text == current_text.text, "test_context_checkout_step_two_is_correct is Failed"
    file.write("test_context_checkout_step_two_is_correct is success \n")


###https://qna.habr.com/q/655465 ПРОВЕРЬ СЕБЯ АНЯ
###https://pythonist.ru/vebskrejping-dlya-sravneniya-czen-na-sajtah-chast-2/

#сверка товаров & цен
def overview():
    item_backpack=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
    cart_item_backpack=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
    item_jacket=driver.find_element(By.XPATH,'//*[@id="item_5_title_link"]/div')
    cart_item_jacket=driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
    if item_backpack==cart_item_backpack and item_jacket==cart_item_jacket:
       file.write("Successful overview \n")
    else:
        file.write("Item error\n")

def parse_price(price_str):
    ###переводим цену в удобный для сравнения формат
    return float(price_str.replace('$', '').replace(',', '').strip())

def price_compare():
    catalogue_backpack=driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
    cart_backpack=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text
    catalogue_jacket=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text
    cart_jacket=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text

    catalogue_backpack_price = parse_price(catalogue_backpack)
    cart_backpack_price = parse_price(cart_backpack)
    catalogue_jacket_price = parse_price(catalogue_jacket)
    cart_jacket_price = parse_price(cart_jacket)

    assert catalogue_backpack_price==cart_backpack_price and catalogue_jacket_price==cart_jacket_price, "price error"
    file.write("Prices are the same")

def total_price_compare(cart_backpack_price, cart_jacket_price):
    total_price=int(cart_backpack_price)+int(cart_jacket_price)
    if total_price==79.98:
        file.write("Total price is correct\n")
    else:
        file.write("Total price is wrong\n")

#финишируем
def finish():
    finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_button.click()
    file.write("Successful order\n")

def test_order_redirect():
    correct_url = 'https://www.saucedemo.com/checkout-complete.html'
    get_url = driver.current_url

    assert correct_url == get_url, "test_order_redirect is Failed"
    file.write("test_order_redirect is success \n")

def test_context_order_is_correct():
    correct_text = "Thank you for your order!"
    current_text = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')

    driver.save_screenshot(f"first_serious_test\\screenshot_context_order_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")
    assert correct_text == current_text.text, "test_context_order_is_correct is Failed"
    file.write("test_context_order_is_correct is success \n")

def back_home():
    backhome_button=driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
    backhome_button.click()
    file.write("Back home successfully\n")

def sc_checkout():
    checkout_step_one()
    test_checkout_step_one_redirect()
    test_context_checkout_step_one_is_correct()
    sleep(2)
    checkout_inside()
    test_checkout_step_two_redirect()
    test_checkout_step_two_is_correct()
    sleep(2)
    overview()
    parse_price()
    price_compare()
    total_price_compare()
    finish()
    test_order_redirect()
    test_context_order_is_correct()
    sleep(2)
    back_home()

#выход из системы
def logout():
        menu_button = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        menu_button.click()
        sleep(2)
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        file.write("Successful logout \n")

def test_logout_redirect():
        correct_url = 'https://www.saucedemo.com/'
        get_url = driver.current_url

        assert correct_url == get_url, "test_logout_redirect is successful"
        file.write("test_logout_redirect is success \n")

def test_context_after_logout_is_correct():
        correct_text = "Accepted usernames are:"
        current_text = driver.find_element(By.XPATH, '//*[@id="login_credentials"]/h4')
        assert correct_text == current_text.text, "test_context_after_logout_is_correct is Failed"
        file.write("test_context_after_logout_is_correct is success \n")

def sc_logout():
        logout()
        test_logout_redirect()
        test_context_after_logout_is_correct()

#итог
set_up()
sleep(2)
sc_login()
sleep(2)
sc_cart()
sleep(2)
sc_checkout()
sleep(2)
sc_logout()

file.close()