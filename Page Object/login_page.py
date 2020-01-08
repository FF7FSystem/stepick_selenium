from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import re

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"
        assert re.findall(r'/login/',self.browser.current_url), "Login link not contains /login/"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form not found"

    def register_new_user(self, email, password):
        input1 = self.browser.find_element_by_xpath("//input[@name='registration-email']")
        input1.send_keys(email)
        input2 = self.browser.find_element_by_xpath("//input[@name='registration-password1']")
        input2.send_keys(password)
        input3 = self.browser.find_element_by_xpath("//input[@name='registration-password2']")
        input3.send_keys(password)

        button = self.browser.find_element_by_xpath("//button[@name='registration_submit']")
        button.click()