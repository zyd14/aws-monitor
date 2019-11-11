import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def sneak_into_aws():

    driver = webdriver.Firefox()

    driver.get('http://console.aws.amazon.com')

    account_input_box = driver.find_element_by_id('resolving_input')
    account_input_box.send_keys(os.getenv('AWS_ADMIN'))
    account_input_box.send_keys(Keys.RETURN)

    try:
        user_input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    except:
        driver.quit()

    user_input_box.send_keys(os.getenv('AWS_USER'))


    sleep(2)
    password_input_box = driver.find_element_by_id('password')
    password_input_box.send_keys(os.getenv('AWS_PASSWORD'))
    password_input_box.send_keys(Keys.RETURN)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'awsc-mezz-data')))
    except:
        driver.quit()

    driver.get('https://us-west-2.console.aws.amazon.com/xray/home?region=us-west-2#/service-map?timeRange=PT1H')
    driver.maximize_window()

def pull_up_dashboard():
    pass

if __name__ == '__main__':
    sneak_into_aws()
