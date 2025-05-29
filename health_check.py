from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # if you want headless mode

# Specify chromedriver path using Service
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

# Your test code here
driver.get("http://18.226.186.67:8081")
print(driver.title)
print('app is running good')

driver.quit()
