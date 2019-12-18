import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def sneak_into_aws():
    
    try:
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        driver.get('http://console.aws.amazon.com')
    
        account_input_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'resolving_input')))
        account_input_box.send_keys(os.getenv('AWS_ADMIN'))
        account_input_box.send_keys(Keys.RETURN)

        user_input_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'username')))
        user_input_box.send_keys(os.getenv('AWS_USER'))

        password_input_box = driver.find_element_by_id('password')
        password_input_box.send_keys(os.getenv('AWS_PASSWORD'))
        password_input_box.send_keys(Keys.RETURN)
    
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'awsc-mezz-data')))
    
        driver.get('https://us-west-2.console.aws.amazon.com/xray/home?region=us-west-2#/service-map?timeRange=PT1H')
        driver.maximize_window()
    
        while True:
            services = ['fastq-registrar-staging']
            zoom_on_service(

            sleep(300)
            refresh_button = driver.find_elements_by_css_selector(".awsui-button-group-content > span:nth-child(1) > span:nth-child(1) > awsui-button:nth-child(1) > button:nth-child(1)")
            refresh_button[0].send_keys(Keys.RETURN)
    except Exception as exc:
        print(f'Error occured while monitoring X-Ray: {exc}')

    driver.quit()

def zoom_on_service(service_name: str):
   service_search_box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'node-graph-filter-input')))
    service_search_box.send_keys(service_name)
    service_search_box.send_keys(Keys.RETURN)
    


def pull_up_dashboard():
    pass

if __name__ == '__main__':
    sneak_into_aws()
