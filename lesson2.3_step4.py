from selenium import webdriver
import time, math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

    allert = browser.switch_to.alert
    allert.accept()

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
