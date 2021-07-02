from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert ('login' in self.browser.current_url), f" 'login' is not presented in URL {self.browser.current_url}"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
         assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

    def register_new_user(self, email, password):
        # Регистрация пользователя
        waite_time = 7
        self.this_element(*LoginPageLocators.REGISTER_EMAIL_FIELD, waite_time).send_keys(email)
        self.this_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD, waite_time).send_keys(password)
        self.this_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD, waite_time).send_keys(password)
        self.this_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON, waite_time).click()
        self.should_be_authorized_user()

