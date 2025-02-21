from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_footer_text():
    driver = webdriver.Chrome()

    try:
        driver.get("https://demoqa.com/")

        wait = WebDriverWait(driver, 10)

        footer_locator = (By.XPATH, "//footer//span")
        footer_element = wait.until(EC.visibility_of_element_located(footer_locator))

        footer_text = footer_element.text

        expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

        assert footer_text == expected_text, f"Текст в подвале не совпадает. Ожидалось: {expected_text}, получено: {footer_text}"

        print("Тест пройден успешно! Текст в подвале совпадает.")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")

    finally:
        # Закрытие браузера
        driver.quit()


        

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
try:
    driver.get("https://demoqa.com/")
    print("Перешли на страницу https://demoqa.com/")

    try:
        elements_button = driver.find_element(By.XPATH, "//h5[text()='Elements']")
        elements_button.click()
        print("Перешли на страницу https://demoqa.com/elements")
    except NoSuchElementException:
        print("Кнопка 'Elements' не найдена на странице.")
        raise
    try:
        center_text = driver.find_element(By.CLASS_NAME, "mb-3").text
        expected_text = "Please select an item from left to start practice."

        if center_text == expected_text:
            print("Текст по центру страницы совпадает с ожидаемым.")
        else:
            print(f"Текст по центру страницы не совпадает. Ожидалось: '{expected_text}', получено: '{center_text}'")
    except NoSuchElementException:
        print("Элемент с текстом не найден на странице.")

    time.sleep(3)
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    driver.quit()
    print("Браузер закрыт.")
