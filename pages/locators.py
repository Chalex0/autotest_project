from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_FORM = (By.ID, "content_inner")
    ADD_TO_BASKET_FORM = (By.ID, "add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
#    PRODUCT_IS_ADDED_TO_BASKET_NAME = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/text()')
#    PRODUCT_IS_ADDED_TO_BASKET_SUM = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

    PRODUCT_IS_ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_IS_ADDED_TO_BASKET_SUM = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')


"""
/html/body/div[2]/div/div[1]/div[1]/div/text()
//*[@id="messages"]/div[1]/div/text()

//*[@id="messages"]/div[3]/div/p[1]/strong
/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong


#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong
#messages > div:nth-child(1) > div > strong

"""