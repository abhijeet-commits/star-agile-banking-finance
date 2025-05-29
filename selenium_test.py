from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser (headless if needed)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://10.0.1.48:8081")  # Replace with real private IP or DNS

    assert "Banking" in driver.title  # Example check
    print("Page loaded successfully with title:", driver.title)
finally:
    driver.quit()
