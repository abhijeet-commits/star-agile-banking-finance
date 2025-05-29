from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Set path to chromedriver explicitly
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

driver.get("http://10.0.1.48:8081")
assert "Banking" in driver.title

driver.quit()
