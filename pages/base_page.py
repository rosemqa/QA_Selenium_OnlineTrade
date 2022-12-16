

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def print_current_url(self):
        current_url = self.driver.current_url
        print(f'Current url {current_url}')

    def assert_url(self, expected_url):
        assert self.driver.current_url == expected_url, 'URL is not correct'
        print('URL is correct')
