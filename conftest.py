import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print('\nStart test')
    driver = webdriver.Chrome()
    yield driver
    print('\nFinish test')
    driver.quit()
