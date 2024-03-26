url = "https://www.footstats.com.br/#/partidas/850/scouts/206504"
#xpath = '//*[@id="main-content"]/app-home/app-nossa-frota'
xpath = '//*[@id="scouts"]/app-scouts-details/div'
xpathAway = '//*[@id="heatmapContainerVisitante"]/canvas'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

# Set up the Selenium webdriver with desired window size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")  # Set window size
driver = webdriver.Chrome(options=chrome_options)  # Or webdriver.Firefox(), etc.
wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds

# Maximize the browser window
driver.maximize_window()

# Load the webpage
driver.get(url)

try:
    # Wait for the specific div element to be visible
    div_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )

    # Get the location and size of the div
    location = div_element.location_once_scrolled_into_view
    size = div_element.size

    # Take a screenshot of the entire page
    driver.save_screenshot('snapshot/screenshot.png')

    # Calculate the cropping dimensions considering the browser window size
    x = int(location['x'])
    y = int(location['y'])
    width = int(size['width'])
    height = int(size['height'])

    # Crop the screenshot to get only the div element
    im = Image.open('snapshot/screenshot.png')
    im = im.crop((x, y, x + width, y + height))

    # Save the cropped image
    im.save('snapshot/div_screenshot.png')

finally:
    # Close the webdriver
    driver.quit()
