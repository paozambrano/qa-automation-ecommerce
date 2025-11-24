from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')

    def login(self, email, password):
        self.type(*self.EMAIL, text=email)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.SUBMIT)