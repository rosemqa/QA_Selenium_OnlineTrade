from pages.main_page import MainPage
from pages.product_listing_page import PLP
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrder
import allure


@allure.description('Product selection and order placement')
def test_buy_product(driver):
    main_page = MainPage(driver)
    main_page.open_plp_usb_flash()

    plp = PLP(driver)
    product_info_plp = plp.select_product()

    cart_page = CartPage(driver)
    product_info_cart = cart_page.continue_checkout_in_the_cart()

    print(product_info_plp, product_info_cart)
    assert product_info_plp[0] == product_info_cart[0], 'Product name in PLP and in the cart is different'
    assert product_info_plp[1] == product_info_cart[1], 'Product price in PLP and in the cart is different'

    pop = PlaceOrder(driver)
    sum_order = pop.place_order()

    assert sum_order == product_info_plp[1], 'Product price in PLP and in the order is different'
