from utilities import OpenTheBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ScrollTo(OpenTheBrowser):

    def currency_conversion_calculator(self):
        element = self.driver.find_element(By.XPATH, '//h1[contains(text(),"Currency exchange calculator")]')
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def bottom(self):
        element = self.driver.find_element_by_class_name('footer-bottom')
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
