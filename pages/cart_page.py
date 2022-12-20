import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    url = 'https://www.onlinetrade.ru/basket.html'

    # LOCATORS
    continue_as_a_guest = '//*[@title="Продолжить без регистрации"]'
    check_box_all_products = '//*[@for="checked_items_all0__ID"]'
    pickup_points_list = '//*[@data-captionfalse="Открыть список всех пунктов выдачи "]'
    pickup_point_3 = '(//label[contains(@class,"ui-checkboxradio-label")])[9]'
    payment_method_cash = '//*[@for="paymentradio1"]'
    place_order = '//*[@name="submit"]'
    product_1_name = '(//a[@class="semibold"])[1]'
    product_1_price = '(//b[@class="nowrap"])[1]'

    # GETTERS
    def get_continue_as_a_guest(self):
        return self.driver.find_element(By.XPATH, self.continue_as_a_guest)

    def get_check_box_all_products(self):
        return self.driver.find_element(By.XPATH, self.check_box_all_products)

    def get_pickup_points_list(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pickup_points_list)))  # self.driver.find_element(By.XPATH, self.pickup_points_list)

    def get_pickup_point_3(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.pickup_point_3))) # element_to_be_clickable((By.XPATH, self.pickup_point_3))) # self.driver.find_element(By.XPATH, self.pickup_point_3)

    def get_payment_method_cash(self):
        return self.driver.find_element(By.XPATH, self.payment_method_cash)

    def get_place_order(self):
        return self.driver.find_element(By.XPATH, self.place_order)

    def get_product_1_name(self):
        return self.driver.find_element(By.XPATH, self.product_1_name)

    def get_product_1_price(self):
        return self.driver.find_element(By.XPATH, self.product_1_price)

    # ACTIONS
    def click_continue_as_a_guest(self):
        self.get_continue_as_a_guest().click()
        print('Click continue as a guest')

    def click_check_box_all_products(self):
        self.get_check_box_all_products().click()
        print('Click check box all products')

    def click_pickup_points_list(self):
        self.get_pickup_points_list().click()
        print('Click pickup points list')

    def click_pickup_point_3(self):
        self.get_pickup_point_3().click()
        print('Select pickup point')

    def click_payment_method_cash(self):
        self.get_payment_method_cash().click()
        print('Select cash payment method')

    def click_place_order(self):
        self.get_place_order().click()
        print('Click place order')

    def should_be_continue_as_a_guest_link(self):
        assert self.is_element_present(self.get_continue_as_a_guest()), 'Continue as a guest link is missing'

    # METHODS
    def select_product(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.print_current_url()
        self.should_be_continue_as_a_guest_link()
        self.click_continue_as_a_guest()
        # time.sleep(3)
        self.get_screenshot()
        self.click_check_box_all_products()
        # time.sleep(3)
        product_name_cart = self.get_product_1_name().text
        product_price_cart = self.get_product_1_price().text
        self.click_pickup_points_list()
        time.sleep(5)
        self.click_pickup_point_3()
        # time.sleep(3)
        self.click_payment_method_cash()
        # time.sleep(3)
        self.click_place_order()
        # time.sleep(3)
        # print(product_name_cart, product_price_cart)
        return product_name_cart, product_price_cart
