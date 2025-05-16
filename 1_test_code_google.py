from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_selenium():
    try:
        print("Setting up Chrome options...")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background (remove to see browser)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        print("Starting Chrome with ChromeDriver...")
        driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)

        test_url = "https://www.wikipedia.org"
        print(f"Opening: {test_url}")
        driver.get(test_url)

        # Take a screenshot
        driver.save_screenshot("chrome_test.png")
        print("Screenshot saved: chrome_test.png")

        print(f"Page title: {driver.title}")
        print("✓ Chrome + ChromeDriver test successful!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_chrome_selenium()
