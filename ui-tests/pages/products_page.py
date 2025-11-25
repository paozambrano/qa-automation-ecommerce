from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_item_name ' )
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')

    def getProductTitle(self):
        return self.get_text(*self.PRODUCT_TITLE)

    def addProduct(self):
        self.click(*self.ADD_TO_CART_BUTTON)
