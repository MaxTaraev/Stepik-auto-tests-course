from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/alert_accept.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
        browser.switch_to.alert.accept()

        x_element = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
        y = calc(x_element)

        browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    finally:
        time.sleep(10)
        browser.quit()
        pass
