from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.fade.in:last-child strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.fade.in:first-child strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')
