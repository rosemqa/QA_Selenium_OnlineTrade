import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from utilities.logger import Logger
import allure


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
        Logger.add_start_step('product_name_in_popup_is_correct')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        product_name_pdp = self.get_product_name().text
        print(product_name_pdp)
        with allure.step('click buy button'):
            self.click_buy_button()
        product_name_popup = self.get_product_info_in_popup().text.split(': ')[1].rstrip('\nЦена')
        print(product_name_popup)
        with allure.step('assert product name on PDP and in popup is the same'):
            assert product_name_pdp == product_name_popup, \
                'product name in popup and on pdp is different'
        print('product name in popup is correct')
        Logger.add_end_step(self.driver.current_url, 'product_name_in_popup_is_correct')

    def product_price_in_popup_is_correct(self):
        Logger.add_start_step('product_price_in_popup_is_correct')
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        # self.print_current_url()

        product_price_pdp = self.get_product_price().text
        print(product_price_pdp)
        # self.click_buy_button()
        product_price_popup = self.get_product_info_in_popup().text.split(': ')[2].rstrip('\nКоличество')
        print(product_price_popup)
        with allure.step('assert product price on PDP and in popup is the same'):
            assert product_price_pdp == product_price_popup, \
                'product price in popup and on pdp is different'
        print('product price in popup is correct')
        Logger.add_end_step(self.driver.current_url, 'product_price_in_popup_is_correct')

    def add_to_compare_changes_to_go_to_compare(self):
        with allure.step('Add to compare link changes to go to compare when clicked'):
            Logger.add_start_step('add_to_compare_changes_to_go_to_compare')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.print_current_url()

            self.assert_text(self.get_compare_link(), 'Сравнить')
            self.click_compare_link()
            time.sleep(2)
            self.assert_text(self.get_compare_link(), 'Перейти к сравнению')
            Logger.add_end_step(self.driver.current_url, 'add_to_compare_changes_to_go_to_compare')

    def remove_from_compare_appears_and_disappears(self):
        with allure.step('Remove from compare icon appears and disappears when clicking compare link'):
            Logger.add_start_step('remove_from_compare_appears_and_disappears')
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
            Logger.add_end_step(self.driver.current_url, 'remove_from_compare_appears_and_disappears')

    def go_to_compare_link_leads_to_compare_page(self):
        with allure.step('Go to compare link leads to compare page'):
            Logger.add_start_step('go_to_compare_link_leads_to_compare_page')
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
            Logger.add_end_step(self.driver.current_url, 'go_to_compare_link_leads_to_compare_page')

    def description_link_opens_description_tab(self):
        with allure.step('description link opens the description tab'):
            Logger.add_start_step('description_link_opens_description_tab')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.print_current_url()

            self.click_description_link()
            assert self.is_element_present(self.description_block), 'description tab is not open'
            print('Description tab is open')
            Logger.add_end_step(self.driver.current_url, 'description_link_opens_description_tab')

    def change_city_for_delivery(self):
        Logger.add_start_step('change_city_for_delivery')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()

        with allure.step('click city for delivery link'):
            self.click_city_for_delivery_link()
        city_for_delivery = self.get_select_city_for_delivery_in_the_popup().text
        with allure.step('click close icon in delivery popup'):
            self.click_close_delivery_popup()
        time.sleep(1)
        assert self.is_not_element_present(self.close_delivery_popup), 'Delivery popup is not closed'
        with allure.step('click city for delivery link'):
            self.click_city_for_delivery_link()
        with allure.step('select city for delivery in popup'):
            self.click_city_for_delivery_in_the_popup()
        time.sleep(1)
        assert self.is_not_element_present(self.close_delivery_popup), 'Delivery popup is not closed'
        city_in_header = self.get_select_city_in_header().text
        with allure.step('assert City in header has been changed'):
            assert city_in_header == city_for_delivery, 'City in header does not match city for delivery'
        Logger.add_end_step(self.driver.current_url, 'change_city_for_delivery')
