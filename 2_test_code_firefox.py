from selenium import webdriver
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.add_argument('--headless')  # Remove this line to see the browser

try:
    print("Starting Firefox with GeckoDriver...")
    driver = webdriver.Firefox(options=options)
   
    print("Navigating to Wikipedia...")
    driver.get("https://www.wikipedia.org/")
   
    print(f"Page title: {driver.title}")
    print("Saving screenshot...")
    driver.save_screenshot("wikipedia_test.png")
   
    print("✓ Test successful!")
    driver.quit()
except Exception as e:
    print(f"Error: {e}")