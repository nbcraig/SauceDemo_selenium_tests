from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class CommonOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
    
    def wait_to_be_clickable(self, locator):
        return self._wait.until(ec.element_to_be_clickable(locator))

    def get_element(self, locator):
        return self.driver.find_element(*locator)
    
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)