from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    PRODUCT_FORM = (By.ID, 'content_inner')
    ADD_TO_BASKET_FORM = (By.ID, 'add_to_basket_form')
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_IS_ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_IS_ADDED_TO_BASKET_SUM = (By.CSS_SELECTOR, 'div.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:first-child') 


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_QUALITY = (By.ID, 'id_form-0-quantity')
