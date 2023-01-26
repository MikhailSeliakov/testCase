import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1280,1000")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    Service_ = Service('chromedriver.exe')
    
    driver = webdriver.Chrome(service=Service_, options=chrome_options)
    yield driver
    driver.quit()