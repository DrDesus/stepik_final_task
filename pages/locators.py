from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.fade.in:last-child strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.fade.in:first-child strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')


class CartPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_CART_MSG = (By.CSS_SELECTOR, '#content_inner > p')
