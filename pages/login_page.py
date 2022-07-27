import time

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()
        self.user_is_registered()

    def should_be_login_url(self):
        assert "/login" in self.url, "login is not in current page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "3irnvpdk7j0ej"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_USER_REPEAT_PASSWORD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        register_link = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_link.click()

    def user_is_registered(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not registered"