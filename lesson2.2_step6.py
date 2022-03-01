from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 120);")

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
