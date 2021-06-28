from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert ('login' in self.browser.current_url), f" 'login' is not present in URL {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
         assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"
