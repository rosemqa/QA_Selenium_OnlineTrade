import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class ProductPage(BasePage):
    url = 'https://www.onlinetrade.ru/catalogue/veb_kamery-c27/logitech/veb_kamera_logitech_webcam_c505e_960_001372' \
          '-2633116.html'

    # LOCATORS
    product_price = '//*[@class="js__actualPrice"]'
    product_name = '//h1[@itemprop="name"]'
    product_info_in_popup = '//*[@class="addedToCart_itemInfo__data"]'
    buy_button = '//span[.="Купить"]'
    compare_link = '//*[contains(@class,"ic__hasSet__compare")]'
    remove_from_compare = '// *[@title="Удалить из сравнения"]'
    compare_table = '// *[@id="compareTableBox_ID"]'
    description_link = '//*[@title="Полное описание и характеристики"]'
    description_block = '//*[@id="tabs_description"]'
    city_for_delivery_link = '(//*[@title="Выбрать другой город"])[1]'
    city_for_delivery_in_the_popup = '//li/a[@title="Санкт-Петербург"]'
    close_delivery_popup = '(//*[@title="Закрыть окно"])[2]'
    select_city_in_header = '//*[@title="Выбрать город"]'

    # GETTERS
    def get_product_price(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_info_in_popup(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_info_in_popup)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_compare_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.compare_link)))

    def get_remove_from_compare(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.remove_from_compare)))

    def get_description_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.description_link)))

    def get_select_city_for_delivery_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.city_for_delivery_link)))

    def get_select_city_for_delivery_in_the_popup(self):
        return WebDriverWait(self.driver, 5).\
            until(EC.element_to_be_clickable((By.XPATH, self.city_for_delivery_in_the_popup)))

    def get_close_delivery_popup(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.close_delivery_popup)))

    def get_select_city_in_header(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select_city_in_header)))

    # ACTIONS
    def click_buy_button(self):
        self.get_buy_button().click()
        print('Click Buy button')

    def click_compare_link(self):
        self.get_compare_link().click()
        print('Click compare link')

    def click_remove_from_compare(self):
        self.get_remove_from_compare().click()
        print('Click "remove from compare"')

    def click_description_link(self):
        self.get_description_link().click()
        print('Click "description link"')

    def click_city_for_delivery_link(self):
        self.get_select_city_for_delivery_link().click()
        print('Click city for delivery link')

    def click_city_for_delivery_in_the_popup(self):
        self.get_select_city_for_delivery_in_the_popup().click()
        print('Click city for delivery in popup')

    def click_close_delivery_popup(self):
        self.get_close_delivery_popup().click()
        print('Close delivery popup')

    # METHODS
    def product_name_in_popup_is_correct(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        product_name_pdp = self.get_product_name().text
        print(product_name_pdp)
        self.click_buy_button()
        product_name_popup = self.get_product_info_in_popup().text.split(': ')[1].rstrip('\nЦена')
        print(product_name_popup)
        assert product_name_pdp == product_name_popup, \
            'product name in popup and on pdp is different'
        print('product name in popup is correct')

    def product_price_in_popup_is_correct(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        # self.print_current_url()

        product_price_pdp = self.get_product_price().text
        print(product_price_pdp)
        # self.click_buy_button()
        product_price_popup = self.get_product_info_in_popup().text.split(': ')[2].rstrip('\nКоличество')
        print(product_price_popup)
        assert product_price_pdp == product_price_popup, \
            'product price in popup and on pdp is different'
        print('product price in popup is correct')

    def add_to_compare_changes_to_go_to_compare(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        self.assert_text(self.get_compare_link(), 'Сравнить')
        self.click_compare_link()
        time.sleep(2)
        self.assert_text(self.get_compare_link(), 'Перейти к сравнению')

    def remove_from_compare_appears_and_disappears(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        # self.print_current_url()

        # self.click_compare_link()
        assert self.is_element_present(self.remove_from_compare), 'Remove from compare button is missing'
        print('"Remove from compare" appears after clicking on "add_to_compare"')
        self.assert_text(self.get_remove_from_compare(), 'Удалить')

        self.click_remove_from_compare()
        time.sleep(1)
        assert self.is_not_element_present(self.remove_from_compare), 'Remove from compare button is present'
        print('"Remove from compare" disappears')

    def go_to_compare_link_leads_to_compare_page(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        # self.print_current_url()

        self.click_compare_link()
        time.sleep(1)
        self.click_compare_link()

        self.print_current_url()
        self.assert_url('https://www.onlinetrade.ru/compare.html?cat_id=27')
        assert self.is_element_present(self.compare_table), 'Compare table is missing'
        print('Compare page is open')

    def description_link_opens_description_tab(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        self.click_description_link()
        assert self.is_element_present(self.description_block), 'description tab is not open'
        print('Description tab is open')

    def change_city_for_delivery(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        self.click_city_for_delivery_link()
        city_for_delivery = self.get_select_city_for_delivery_in_the_popup().text
        print(city_for_delivery)
        self.click_close_delivery_popup()
        time.sleep(1)
        assert self.is_not_element_present(self.close_delivery_popup), 'Delivery popup is not closed'
        self.click_city_for_delivery_link()
        self.click_city_for_delivery_in_the_popup()
        time.sleep(1)
        assert self.is_not_element_present(self.close_delivery_popup), 'Delivery popup is not closed'
        city_in_header = self.get_select_city_in_header().text
        assert city_in_header == city_for_delivery, 'City in header does not match city for delivery'
