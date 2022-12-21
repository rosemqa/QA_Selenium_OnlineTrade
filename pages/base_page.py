import datetime
import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def print_current_url(self):
        current_url = self.driver.current_url
        print(f'Current url {current_url}')

    def assert_url(self, expected_url):
        assert self.driver.current_url == expected_url, 'URL is not correct'
        print('URL is correct')

    def get_screenshot(self):
        # time.sleep(2)
        now_date = datetime.datetime.now().strftime('%d.%m.%Y.%H.%M.%S')
        screenshot_name = f'screenshot{now_date}.png'
        self.driver.save_screenshot('screenshots\\' + screenshot_name)

    # Метод для проверки наличия элемента на странице
    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException:
            return False
        return True
