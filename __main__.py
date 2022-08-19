
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import sys
import pickle
import pandas as pd
import traceback

def get_driver():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(
                service = Service(ChromeDriverManager().install()),
                options = chrome_options)
    driver.implicitly_wait(5)
    return driver

def ingest_data(driver, row):

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

    we_checkbox = driver.find_element(
        by = By.XPATH,
        value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[5]/mat-checkbox/label/div/input'
    )
    driver.execute_script("arguments[0].click();", we_checkbox)

    we_submit_button = driver.find_element(
        by = By.XPATH,
        value = '/html/body/app-root/div/div/div[1]/app-hgsform/div[1]/div[2]/form/div/div[6]/button'
    )
    driver.execute_script("arguments[0].click();", we_submit_button)

    is_applied = driver.find_element(
        by = By.XPATH,
        value = '/html/body/app-root/div/div/div[1]/app-applied/div/p'
    )
    time.sleep(3)
    if is_applied.text == 'Job Applied':
        return 'Success'
    return 'Failure'


def main():
    print('Successful initialized driver')
    df = pd.read_csv('Invalid_leads.csv')
    print('Successfully read the input csv file')
    print(df.head())

    status = []
    for index, row in df.iterrows():
        row['first_name'] = process(row['first_name'])
        try:
            driver = get_driver()
            application_status = ingest_data(driver, row)
            status.append(application_status)
        except:
            status.append('Failure')
            traceback.print_exc()
        finally:
            driver.close()

        df['status'] = pd.Series(status)
        df.to_csv('hgs_output_invalid_leads.csv',index=False)

if __name__=='__main__':
    main()
