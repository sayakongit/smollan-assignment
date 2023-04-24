from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, os
import pandas as pd

DRIVER_PATH = r"C:\Users\hp\Desktop\chromedriver.exe"
URL = ' https://www.vodafone.co.uk/mobile/phones/pay-monthly-contracts'


try:
    # Setting up the chrome driver
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.maximize_window()
    driver.get(URL)
    
    time.sleep(5)
    
    # Accepting the cookies
    button = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
    button.click()
    
    # Scrolling to the last element
    scroll_count = 0
    while scroll_count < 12:
        elems = driver.find_elements_by_xpath('//*[starts-with(@class, "vfuk-DeviceCard__wrapper")]')
        last_elem = elems[-1]
        last_elem.location_once_scrolled_into_view
        
        time.sleep(2)
        scroll_count += 1
    
    
    # Searching and getting the urls from the listings    
    all_listings = driver.find_elements_by_xpath('//*[starts-with(@class, "vfuk-DeviceCard__wrapper")]')
    
    data = []
    for listing in all_listings:
        product = listing.get_attribute('aria-label')
        product_url = listing.get_attribute('href')
        data.append([product, product_url])
        
    # Sorting the urls and storing into CSV
    data = sorted(data, key = lambda x : x[1])
    try:
        my_df = pd.DataFrame(data)
        headerList=['Product Name','Product URL']
        file_name = f'Product_Data.csv'
        my_df.to_csv(file_name, index=False, header=headerList)
    except Exception as e:
        print(f'Error in Pandas --> {e}')
    
    new_data = data[:3]
    
    for each in new_data:
        product_name, new_url = each
        driver.get(new_url)
        
        time.sleep(5)
        
        path = f'./{product_name}'
        os.mkdir(path)
        
        driver.save_screenshot(f"{product_name}/PDP.png")
        
        try:
            # after clicking on "Pay for your phone in one go" and then close the popup
            first_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[3]/div/div/div/div[3]/div[4]/div[4]/div/div[2]/a')
            first_btn.click()
            time.sleep(2)
            driver.save_screenshot(f"{product_name}/MSRP.png")
            
            close_btn = driver.find_element_by_xpath('//*[@class="vfuk-Modal__close"]')
            close_btn.click()
            time.sleep(2)

            # Click on "Build your Phone Plan"
            second_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[3]/div/div/div/div[3]/div[4]/div[4]/div/div[1]/div/button')
            second_btn.click()
            time.sleep(6)

            # Click on "I'm a new customer".
            third_btn = driver.find_element_by_xpath('//button[@data-testid="newOrExisting-cta-new"]')
            third_btn.click()
            time.sleep(4)
            driver.save_screenshot(f"{product_name}/Phoneplan.png")
            time.sleep(4)
            
        except Exception as e:
            print('Error -->', e)
            continue
        
        # Click on "Continue"
        fourth_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[4]/div/div/div[2]/button')
        fourth_btn.click()
        time.sleep(2)
        
        # Click on "NO" button
        fifth_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div[4]/div/div/div/div[3]/div/div/button[2]')
        fifth_btn.click()
        time.sleep(2)
        driver.save_screenshot(f"{product_name}/Airtime.png")
        time.sleep(2)
        
        
except Exception as e:
    print('Error -->', e)
    
finally:
    driver.quit()
    
