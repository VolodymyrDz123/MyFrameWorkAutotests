from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/uk/accounts/login/", "No login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "the login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "the register form is absent"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        confirm_password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        submit_button.click()
