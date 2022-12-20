import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MainPage(BasePage):
    url = 'https://www.onlinetrade.ru/'

    # LOCATORS
    menu_catalog = '//*[@class="header__menuLink__icon"]'
    sub_menu_computers = '//*[@data-catid="243"]'
    item_usb_flash = '//*[@title="Перейти в категорию «Флеш-диски USB»"]'

    # GETTERS
    def get_menu_catalog(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.menu_catalog)))

    def get_sub_menu_computers(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.sub_menu_computers)))

    def get_item_usb_flash(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.item_usb_flash)))

    # ACTIONS
    def click_menu_catalog(self):
        self.get_menu_catalog().click()
        print('Click menu catalog')

    def hover_sub_menu_computers(self):
        ActionChains(self.driver).move_to_element(self.get_sub_menu_computers()).perform()
        print('Hover over sub menu computers')

    def click_item_usb_flash(self):
        self.get_item_usb_flash().click()
        print('Click Usb Flash item')

    # METHODS
    def open_plp_usb_flash(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.print_current_url()
        self.click_menu_catalog()
        # time.sleep(3)
        self.hover_sub_menu_computers()
        # time.sleep(3)
        self.click_item_usb_flash()
        # time.sleep(3)
        self.assert_url('https://www.onlinetrade.ru/catalogue/flesh_diski_usb-c158/')

