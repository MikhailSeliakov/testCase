from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/search/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def getMainPage(self):
        return self.driver.get(self.base_url)
    
    def getCurrentURL(self):
        return self.driver.current_url

    def switchContent_(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])