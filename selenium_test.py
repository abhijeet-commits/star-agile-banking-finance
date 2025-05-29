from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import tempfile

# Create a unique temporary directory for Chrome user data
temp_user_data_dir = tempfile.mkdtemp()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f'--user-data-dir={temp_user_data_dir}')  # Avoid profile lock errors

# Initialize Chrome driver with service and options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("http://18.226.186.67:8081")  # Replace with your real IP/DNS

    assert "Banking" in driver.title  # Simple title check
    print("Page loaded successfully with title:", driver.title)
finally:
    driver.quit()
