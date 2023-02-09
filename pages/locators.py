from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    COMPLETE_NAME_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    COMPLETE_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                       "p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")
