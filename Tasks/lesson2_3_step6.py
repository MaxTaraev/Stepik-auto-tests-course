from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/redirect_accept.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.trollface').click()

        browser.switch_to.window(browser.window_handles[1])

        x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
        x = int(x_element.text)
        y = calc(x)

        answer = browser.find_element(By.CSS_SELECTOR, '#answer.form-control')
        answer.send_keys(y)

        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
    finally:
        time.sleep(10)
        browser.quit()
        pass
