from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "https://SunInJuly.github.io/execute_script.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        button = browser.find_element(By.TAG_NAME, 'button')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()


        # x_element = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
        # x = int(x_element.get_attribute('valuex'))
        # y = calc(x)

        # answer = browser.find_element(By.CSS_SELECTOR, '#answer')
        # answer.send_keys(y)

        # im_robot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox.check-input')
        # im_robot.click()

        # robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule.check-input')
        # robots_rule.click()

        # submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default[type="submit"]')
        # submit.click()


        # input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        # input1.send_keys('TEXT')

        # input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        # input2.send_keys('TEXT TEXT')

        # input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        # input3.send_keys('TEXT TEXT TEXT')

        # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # button.click()

        # time.sleep(1)

        # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # welcome_text = welcome_text_elt.text

        # assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        browser.quit()
