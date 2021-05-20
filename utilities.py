from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class OpenTheBrowser:

        driver = webdriver.Chrome('chromedriver.exe')
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        def go_to_site(self):
                self.driver.get('https://www.paysera.bg/v2/en-LT/fees/currency-conversion-calculator')
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"Currency exchange calculator")]')))
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))

        def close_browser(self):
                time.sleep(2)
                self.driver.close()