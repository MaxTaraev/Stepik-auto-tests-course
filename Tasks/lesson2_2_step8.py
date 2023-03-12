from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/file_input.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"][required]').send_keys('TEST')
        browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"][required]').send_keys('TEST')
        browser.find_element(By.CSS_SELECTOR, 'input[name="email"][required]').send_keys('TEST')

        directory = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(directory, 'lesson2_2_bio.txt')

        browser.find_element(By.CSS_SELECTOR, '#file[required]').send_keys(file)    

        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
    finally:
        time.sleep(10)
        browser.quit()
        pass
