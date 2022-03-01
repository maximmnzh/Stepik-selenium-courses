from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(2)
    button.click()
    time.sleep(2)

finally:
    time.sleep(2)
    browser.quit()
