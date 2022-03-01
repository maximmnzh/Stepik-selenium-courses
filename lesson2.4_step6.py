from selenium import webdriver
import time, math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "#button").click()

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
