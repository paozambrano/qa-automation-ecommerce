from pages.products_page import ProductsPage
from pages.login_page import LoginPage

def test_add_product_to_cart(driver, base_url):
    driver.get(base_url)

    lp = LoginPage(driver)
    lp.login("standard_user", "secret_sauce")

    pp = ProductsPage(driver)

    product_title = pp.getProductTitle()
    assert product_title is not None

    pp.addProduct()


