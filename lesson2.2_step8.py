from selenium import webdriver
import time, os

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("Ivan@")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
