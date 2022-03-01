from selenium import webdriver
import time, math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "#verify").click()

    message = browser.find_element(By.CSS_SELECTOR, "#verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
