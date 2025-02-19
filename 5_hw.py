from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def check_elements_on_page():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")

        if username_field and password_field and submit_button:
            print("Элементы найдены")

    except NoSuchElementException as e:
        print(f"Ошибка: элемент не найден - {e}")

check_elements_on_page()
