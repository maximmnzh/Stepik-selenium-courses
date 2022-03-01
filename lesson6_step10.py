from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > [placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > [placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > [placeholder='Input your email']")
    input3.send_keys("Smolensk@123.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(2)
    button.click()
    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

#except Exception as error:
    #print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(5)
    browser.close()
    browser.quit()
