import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("123")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
