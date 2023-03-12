from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

if __name__ == '__main__':

    link = "http://suninjuly.github.io/huge_form.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        elements = browser.find_elements(By.CSS_SELECTOR, 'input')
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


        # input1 = browser.find_element(By.TAG_NAME, value1)
        # input1.send_keys("Ivan")
        # input2 = browser.find_element(By.NAME, value2)
        # input2.send_keys("Petrov")
        # input3 = browser.find_element(By.CLASS_NAME, value3)
        # input3.send_keys("Smolensk")
        # input4 = browser.find_element(By.ID, "country")
        # input4.send_keys("Russia")
        # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
