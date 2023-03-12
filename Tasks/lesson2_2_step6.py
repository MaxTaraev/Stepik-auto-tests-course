from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/execute_script.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
        x = int(x_element.text)
        y = calc(x)

        robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
        browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
        robots_rule.click()

        robots_check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

        answer = browser.find_element(By.CSS_SELECTOR, '#answer.form-control')
        answer.send_keys(y)

        submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
        submit.click()

        # print(os.path.abspath(__file__))
        # print(os.path.abspath(os.path.dirname(__file__)))

    finally:
        time.sleep(10)
        browser.quit()
        pass
