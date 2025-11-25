from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage (BasePage):
    cart_btn = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    checkout_btn = (By.ID, 'checkout')

    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    zip_code = (By.ID, 'postal-code')
    continue_btn = (By.ID, 'continue')

    def goToCart(self):
        self.click(*self.cart_btn) 
    
    def checkOut (self):
        self.click(*self.checkout_btn)

    def checkOut_info(self, name, lastName, zipCode):
        self.type(*self.first_name, text=name)
        self.type(*self.last_name, text=lastName)
        self.type(*self.zip_code, text=zipCode)
        self.click(*self.continue_btn)

    