from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert ('catalogue' in self.browser.current_url), f" 'basket' is not present in URL {self.browser.current_url}"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_QUALITY), 'Basket is not empty'

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
                                                                     'Basket is empty message not presented'

    def should_not_be_is_empty_message(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
                                                                     'Basket is empty is presented, but should not be'

    def should_not_disappeare_message(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
                                                                      'Basket is empty is presented, but disappeared'





