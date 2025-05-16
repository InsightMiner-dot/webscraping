from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_chrome():
    try:
        print("Setting up Chrome...")
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment to run in background
       
        # Specify path to chromedriver.exe (if not in PATH)
        service = Service(executable_path=r'C:\path\to\chromedriver.exe')
       
        driver = webdriver.Chrome(service=service, options=chrome_options)
       
        print("Opening Wikipedia...")
        driver.get("https://www.wikipedia.org")
       
        print(f"Title: {driver.title}")
        driver.save_screenshot("chrome_test.png")
        print("Screenshot saved: chrome_test.png")
       
        print("✓ Chrome test successful!")
       
    except Exception as e:
        print(f"❌ Chrome test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_chrome()
