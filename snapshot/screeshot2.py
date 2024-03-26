from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_div_screenshot(url, div_xpath_home,div_xpath_away, output_filename_home,output_filename_away):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")  
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)  
    wait = WebDriverWait(driver, 10) 

    try:
        driver.get(url)
        driver.maximize_window()  

        div_element = wait.until(EC.presence_of_element_located((By.XPATH, div_xpath_home)))
        div_element.screenshot(output_filename_home)
        
        div_element = wait.until(EC.presence_of_element_located((By.XPATH, div_xpath_away)))
        div_element.screenshot(output_filename_away)

    finally:
        driver.quit()

url = "https://localhost:5001/finalizacao?idChampionship=904&idMatch=210357"
div_xpath_home = '/html/body/div/main/div[4]'  
div_xpath_away = '/html/body/div/main/div[5]'
output_filename_home = "screen_div_home.png"
output_filename_away = "screen_div_away.png"
capture_div_screenshot(url, div_xpath_home,div_xpath_away, output_filename_home,output_filename_away)
