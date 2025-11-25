from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_cart_checkOut (driver, base_url):
    driver.get(base_url)

    lp = LoginPage(driver)
    lp.login("standard_user", "secret_sauce")

    cp = CartPage(driver)
    cp.goToCart()
    cp.checkOut()
    cp.checkOut_info('Paola', 'Zambrano', 18061)

    assert 'checkout-step-two' in driver.current_url