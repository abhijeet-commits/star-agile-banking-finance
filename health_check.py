from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://10.0.1.48:8081")  # Replace with actual app-server private IP
    assert "Banking" in driver.title
    print("Health check passed.")
except Exception as e:
    print("Health check failed:", e)
finally:
    driver.quit()
