from pages.main_page import MainPage


def test_buy_product(driver):
    main_page = MainPage(driver)
    main_page.open_plp_usb_flash()

