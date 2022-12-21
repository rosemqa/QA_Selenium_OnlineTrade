import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlaceOrder(BasePage):

    # LOCATORS
    delivery_date_dropdown = '//*[@id="delivery_date"]'
    contact_name = '//*[@id="contact__ID"]'
    phone_number = '//*[@id="cellphone__ID"]'
    sms_time_dropdown = '//*[@id="sms_time__ID"]'
    email = '//*[@id="email__ID"]'
    submit_order = '//*[@id="order_step2_submit"]'
    product_cost = '(//span[@class="semibold"])[1]'

    # GETTERS
    def get_delivery_date_dropdown(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.delivery_date_dropdown)))

    def get_contact_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.contact_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_sms_time_dropdown(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sms_time_dropdown)))

    def get_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_submit_order(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.submit_order)))

    def get_product_cost(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.product_cost)))

    # ACTIONS
    def select_delivery_date(self):
        Select(self.get_delivery_date_dropdown()).select_by_index(1)
        print('Select delivery date')

    def enter_contact_name(self):
        self.get_contact_name().send_keys('Test Tests')
        print('Enter contact name')

    def enter_phone_number(self):
        self.get_phone_number().send_keys(88000000000)
        print('Enter phone number')

    def select_sms_time(self):
        Select(self.get_sms_time_dropdown()).select_by_index(1)
        print('Select sms time')

    def enter_email(self):
        self.get_email().send_keys('test@mail.com')
        print('Enter email')

    def click_submit_order(self):
        self.get_submit_order().click()
        print('Click submit order')

    def should_be_submit_order_button(self):
        assert self.is_element_present(self.submit_order), 'Submit order button is missing'

    # METHODS
    def place_order(self):
        self.print_current_url()
        # time.sleep(3)
        self.select_delivery_date()
        # time.sleep(3)
        self.enter_contact_name()
        # time.sleep(3)
        self.enter_phone_number()
        # time.sleep(3)
        self.select_sms_time()
        # time.sleep(3)
        self.enter_email()
        self.get_screenshot()
        self.should_be_submit_order_button()
        sum_order = self.get_product_cost().text
        time.sleep(3)
        # print(sum_order)
        return sum_order
