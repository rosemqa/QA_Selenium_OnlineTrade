import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class PLP(BasePage):
    url = 'https://www.onlinetrade.ru/catalogue/flesh_diski_usb-c158/'

    # LOCATORS
    filter_in_stock = '//*[@id="l5950a4a1de00bc24202c5f78a0a726be"]'
    filter_producer = '//*[@id="l0da810b30a84539a60a1c03da2ee0e22"]'
    filter_price = '//*[@data-spoiledcontent="price_active"]'
    filter_price_from = '//*[@id="price1"]'
    filter_price_to = '//*[@id="price2"]'
    filter_size_1 = '//*[@id="la663fd9d3153c026d16655af9b2fece0"]'
    filter_size_2 = '//*[@id="l5dd8082342600383ac354a79528aa0a5"]'
    apply_filters = '//*[@title="Подобрать"]'
    sort_list = '//*[@id="js__listingSort_ID"]'
    buy_button_1 = '(//*[@data-handler="buy"])[1]'
    popup_buy = '//*[@id="popup_buy"]'
    checkout_button_in_popup = '//*[@title="Оформить заказ"]'
    product_1_name = '(//*[@class="indexGoods__item__name  "])[1]'
    product_1_price = '(//*[@itemprop="price"])[1]'

    # GETTERS
    def get_filter_in_stock(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_in_stock)))

    def get_filter_producer(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_producer)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_filter_price_from(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_from)))

    def get_filter_price_to(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_to)))

    def get_filter_size_1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_1)))

    def get_filter_size_2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_2)))

    def get_apply_filters(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters)))

    def get_sort_list(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sort_list)))

    def get_buy_button_1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.buy_button_1)))

    def get_popup_buy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.popup_buy)))

    def get_checkout_button_in_popup(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button_in_popup)))

    def get_product_1_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price)))

    # ACTIONS
    def select_filter_in_stock(self):
        self.get_filter_in_stock().click()
        print('Select in stock filter')

    def select_filter_producer(self):
        self.get_filter_producer().click()
        print('Select producer filter')

    def open_filter_price(self):
        self.get_filter_price().click()
        print('Open price filter')

    def clear_filter_price_from(self):
        self.get_filter_price_from().clear()
        print('Clear price filter from')

    def clear_filter_price_to(self):
        self.get_filter_price_to().clear()
        print('Clear price filter to')

    def enter_filter_price_from(self):
        self.get_filter_price_from().send_keys(250)
        print('Enter price filter from')

    def enter_filter_price_to(self):
        self.get_filter_price_to().send_keys(1500)
        print('Enter price filter to')

    def select_filter_size_1(self):
        self.get_filter_size_1().click()
        print('Select size 1 filter')

    def select_filter_size_2(self):
        self.get_filter_size_2().click()
        print('Select size 2 filter')

    def click_apply_filters(self):
        self.get_apply_filters().click()
        print('Click apply filters')

    def sort_by_price_asc(self):
        Select(self.get_sort_list()).select_by_value('price-asc')
        print('Sort by price asc')

    def click_buy_button_1(self):
        self.get_buy_button_1().click()
        print('Click buy button 1')

    def click_checkout_button_in_popup(self):
        self.get_checkout_button_in_popup().click()
        print('Click checkout button in popup')

    # METHODS
    def select_product(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.print_current_url()
        self.select_filter_in_stock()
        # time.sleep(3)
        self.select_filter_producer()
        # time.sleep(3)
        self.open_filter_price()
        # time.sleep(3)
        self.clear_filter_price_from()
        self.clear_filter_price_to()
        # time.sleep(3)
        self.enter_filter_price_from()
        self.enter_filter_price_to()
        # time.sleep(3)
        self.select_filter_size_1()
        self.select_filter_size_2()
        time.sleep(3)
        self.click_apply_filters()
        # time.sleep(3)
        self.sort_by_price_asc()
        # time.sleep(3)
        product_name_plp = self.get_product_1_name().text
        product_price_plp = self.get_product_1_price().text
        self.click_buy_button_1()
        # time.sleep(3)
        self.click_checkout_button_in_popup()
        # time.sleep(3)
        # assert 'https://www.onlinetrade.ru/basket.html?basket_hash=' in self.driver.current_url
        # print(product_name_plp, product_price_plp)
        return product_name_plp, product_price_plp
