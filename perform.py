import time
from utilities import OpenTheBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GetTheValueFrom(OpenTheBrowser):

    def sell_field(self):
        return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[1]/input').get_attribute("value")

    def buy_field(self):
        return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[3]/input').get_attribute("value")

    def sell_selected_currency(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[1]/div/div[1]/span/span[2]/span').text

    def buy_selected_currency(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[3]/div/div[1]/span/span[2]/span').text

    def currency_table(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]').text

    def bank_provider_rate_difference_with_paysera(self):
        time.sleep(2)
        try:
            st = self.driver.find_element_by_xpath(
                '//*[@id="currency-exchange-app"]/div/div/div[2]/table/tbody/tr/td[5]/span/span/span[2]').text
            return float(st.strip("()"))
        except:
            return 0

    def warning(self):
        try:
            return self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]/div/div/div[1]/div/div/div/span/span').text
        except:
            return 0


class InsertValueInto(OpenTheBrowser):

    def sell_field(self, value='500'):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[1]/input').send_keys(value)
        time.sleep(2)

    def buy_field(self, value='100'):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[3]/input').send_keys(value)
        time.sleep(2)


class EraseTheValueFrom(OpenTheBrowser):

    def sell_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[1]/input').clear()
        time.sleep(2)

    def buy_field(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]//*/form/div[3]/input').clear()
        time.sleep(2)


class ClickOn(OpenTheBrowser):

    def filter_btn(self):
        self.driver.find_element_by_xpath('//button[contains(text(),"Filter")]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        time.sleep(5)

    def clear_filter_btn(self):
        self.driver.find_element_by_xpath('//button[contains(text(),"Clear filter")]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="currency-exchange-app"]//table/tbody/tr[1]/td[1]')))
        time.sleep(5)

    def sell_currency_selection(self):
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[1]/div/div[1]/span').click()
        time.sleep(2)

    def all_from_sell_selection_list(self):
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-0-0"]/span').click()
        time.sleep(2)

    def cad_from_sell_selection_list(self):
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-0-13"]/span').click()
        time.sleep(2)

    def buy_currency_selection(self):
        self.driver.find_element_by_xpath('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[3]/div/div[1]/span').click()
        time.sleep(2)

    def all_from_buy_selection_list(self):
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-1-0"]/span').click()
        time.sleep(2)

    def usd_from_buy_selection_list(self):
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-1-2"]/span').click()
        time.sleep(2)

    def eur_from_buy_selection_list(self):
        self.driver.find_element_by_xpath('//*[@id="ui-select-choices-row-1-1"]/span').click()
        time.sleep(2)

    def localization_btn(self):
        self.driver.find_element_by_class_name('js-localization-popover').click()
        time.sleep(2)

    def countries_dropdown_btn(self):
        self.driver.find_element_by_id('countries-dropdown').click()
        time.sleep(2)

    def United_kingdom_btn(self):
        self.driver.find_element_by_partial_link_text('United Kingdom').click()
        time.sleep(2)
