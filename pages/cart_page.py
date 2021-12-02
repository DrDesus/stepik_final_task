from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), "Cart is not empty"

    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MSG), "Message about empty cart is not present"

