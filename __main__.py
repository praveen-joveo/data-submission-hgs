
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import sys
import pickle
import pandas

# class GenerateKiteToken(object):
#     def execute(self, parser, unknown):
#
#         kite =  KiteConnect(api_key=env.KITE_APIKEY)
#
#         driver.get(kite.login_url())
#         webelement_username = driver.find_element(
#                                 by=By.XPATH,
#                                 value='/html/body/div[1]/div/div[2]/div[1]/div\
#                                        /div/div[2]/form/div[1]/input')
#         webelement_username.send_keys(env.KITE_USERID)
#         time.sleep(1)
#         webelement_password = driver.find_element(
#                                 by=By.XPATH,
#                                 value='/html/body/div[1]/div/div[2]/div[1]/div\
#                                        /div/div[2]/form/div[2]/input')
#
#         webelement_password.send_keys(env.KITE_PASSWORD)
#         time.sleep(1)
#         driver.find_element(
#                         by=By.XPATH,
#                         value='/html/body/div[1]/div/div[2]/div[1]/div/div\
#                                /div[2]/form/div[4]/button').click()
#         webelement_pin = driver.find_element(
#                             by=By.XPATH,
#                             value='/html/body/div[1]/div/div[2]/div[1]/div/div\
#                                    /div[2]/form/div[2]/div/input')
#         webelement_pin.send_keys(env.KITE_TPIN)
#         time.sleep(1)
#         driver.find_element(
#                             by=By.XPATH,
#                             value='/html/body/div[1]/div/div[2]/div[1]/div/div\
#                                    /div[2]/form/div[3]/button').click()
#         time.sleep(1)
#         request_token = driver.current_url.split(
#                                 'request_token=')[1].split('&')[0]
#         session = kite.generate_session(
#                         request_token,
#                         api_secret=env.KITE_APISECRET)
#         kite.set_access_token(access_token = session['access_token'])
#         pickle.dump(kite,open(env.KITE_PATH,'wb'))
#         driver.implicitly_wait(5)
#         driver.quit()

def get_driver():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-logging')
    driver = webdriver.Chrome(
                service = Service(ChromeDriverManager().install()),
                options = chrome_options)
    driver.implicitly_wait(5)
    return driver

def main():
    driver = get_driver()
    print('Successful initialized driver')
    df = pandas.read_csv('hgs_input.csv')
    print('Successfully read the input csv file')
    print(df.head())

    for index, row in df.iterrows():
        driver.get(row['url'])

        we_email = driver.find_element(
            by = By.XPATH,
            value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[1]/div/div/mat-form-field/div/div/div/input'
        )
        we_email.send_keys(row['email'])
        we_firstname = driver.find_element(
            by = By.XPATH,
            value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[2]/div/div/mat-form-field/div/div/div/input'
        )
        we_firstname.send_keys(row['first_name'])

        we_lastname = driver.find_element(
            by = By.XPATH,
            value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[3]/div/div/mat-form-field/div/div/div/input'
        )
        we_lastname.send_keys(row['last_name'])

        # we_country_code = driver.find_element(
        #     by = By.XPATH,
        #     value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[3]/div/div/mat-form-field/div/div/div/input'
        # )
        # we_country_code.send_keys('+1')

        we_ph_number = driver.find_element(
            by = By.XPATH,
            value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[4]/div/div/div[1]/app-phone-number/form/mat-form-field[2]/div/div[1]/div/input'
        )
        we_ph_number.send_keys(row['phone_number'])

        # we_checkbox = driver.find_element(
        #     by = By.XPATH,
        #     value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[5]/mat-checkbox/label/div/input'
        # )
        we_checkbox = driver.find_element_by_id('mat-checkbox-1-input')
        we_checkbox.click()

        # we_submit_button = driver.find_element(
        #     by = By.XPATH,
        #     value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[6]/button'
        # )
        # we_submit_button.click()
        time.sleep(2)


if __name__=='__main__':
    main()
