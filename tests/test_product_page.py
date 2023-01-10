from pages.product_page import ProductPage


def test_add_to_compare(driver):
    page = ProductPage(driver)
    page.add_to_compare_changes_to_go_to_compare()
    page.remove_from_compare_appears_and_disappears()
    page.go_to_compare_link_leads_to_compare_page()


def test_product_info_in_popup(driver):
    page = ProductPage(driver)
    page.product_name_in_popup_is_correct()
    page.product_price_in_popup_is_correct()


def test_product_description(driver):
    page = ProductPage(driver)
    page.description_link_opens_description_tab()


def test_change_city_for_delivery(driver):
    page = ProductPage(driver)
    page.change_city_for_delivery()

