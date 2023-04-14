from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, os
from cookies import latest_cookies

DRIVER_PATH = r"C:\Users\hp\Desktop\chromedriver.exe"
URL = 'https://shop.ee.co.uk/mobile-phones/pay-monthly/iphone-14-pro-5g/details?CTTag=CT_Sal_HP_H2_Phones_C5_AppleiPhone14Pro_Q4_2023'


try:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.maximize_window()
    driver.get(URL)
    
    for cookie in latest_cookies:
        driver.add_cookie(cookie)
        
    driver.get(URL)
    
    product_area = driver.find_element_by_xpath('//span[@data-content-id="product-title"]')
    product = product_area.text
    
    variants = driver.find_elements_by_xpath('//div[starts-with(@class, "m17-nav-item")]//strong')
    button = driver.find_element_by_xpath('//*[@data-testid="show-viewAllPlans"]')
    
    path = f'./{product}'
    os.mkdir(path) 
    
    for i in range(len(variants)):
        variant = variants[i].text
        variants[i].click()
        time.sleep(5)
        button.click()
        
        driver.execute_script("$('.not-handheld').css('zoom', 0.2);")
        driver.execute_script("$('#_15gifts-overlay').hide();")
        
        product_area.location_once_scrolled_into_view
        driver.save_screenshot(f"{product}/{product}_{variant}.png")
        driver.execute_script("$('.not-handheld').css('zoom', 1);")
        button.click()

except Exception as e:
    print('Error -->', e)
    
finally:
    driver.quit()
    
