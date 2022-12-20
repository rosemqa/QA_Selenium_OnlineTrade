import datetime
import time
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

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

    def is_element_present(self, getter):
        try:
            getter
        except NoSuchElementException:
            return False
        return True
