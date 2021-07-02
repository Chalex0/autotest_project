from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_form()
        self.should_be_product_form()
        self.should_be_add_to_basket_button()

    def should_be_product_url(self):
        # Проверка на корректный url
        assert ('catalogue' in self.browser.current_url), f"'catalogue' is not present in URL{self.browser.current_url}"

    def should_be_add_to_basket_form(self):
        # Должна быть форма для добавления в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), \
                                       "ADD_TO_BASKET_FORM is not presented"

    def should_be_product_form(self):
        # Должна быть форма описания продукта
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM), "PRODUCT_FORM is not presented"    

    def should_be_add_to_basket_button(self):
        # Должна быть кнопка для добавления в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
                                        "ADD_TO_BASKET_BUTTON is not presented"

    def product_add_to_basket(self):
        # Добавить товар в корзину и расчитать код
        button = self.this_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def product_is_added_to_basket_check_sum(self):
        # Сравнить стоимость в корзине с ценой добавленного товара
        sum_in_basket = self.this_element(*ProductPageLocators.PRODUCT_IS_ADDED_TO_BASKET_SUM)
        product_price = self.this_element(*ProductPageLocators.PRODUCT_PRICE)
        assert  sum_in_basket.text == product_price.text, "PRODUCT_IS_ADDED_TO_BASKET_SUM is not equal PRODUCT_PRICE"
      
    def product_is_added_to_basket_check_name(self):
        # Сравнить название товара с названием в корзине
        product_in_basket_name = self.this_element(*ProductPageLocators.PRODUCT_IS_ADDED_TO_BASKET_NAME)
        product_name = self.this_element(*ProductPageLocators.PRODUCT_NAME)
        assert  product_in_basket_name.text == product_name.text, "PRODUCT_IS_ADDED_TO_BASKET_NAME \
                                                                   is not equal PRODUCT_NAME"

    def should_not_be_success_message(self):
        # Сообщения не должно быть на странице
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is \
                                                                                   presented, but should not be"

    def should_not_disappeare_message(self):
        # Сообщение не исчезает со страницы
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),'Success message is presented, but disappeared'

