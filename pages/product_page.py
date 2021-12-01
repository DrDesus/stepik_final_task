from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.click_on_button(*ProductPageLocators.ADD_TO_CART)
        self.solve_quiz_and_get_code()
        self.does_the_price_match()
        self.does_the_name_match()

    def does_the_name_match(self):
        assert self.get_text_of_element(*ProductPageLocators.NAME_PRODUCT) == \
               self.get_text_of_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), 'Name product not match'

    def does_the_price_match(self):
        assert self.get_text_of_element(*ProductPageLocators.PRICE_PRODUCT) == \
               self.get_text_of_element(*ProductPageLocators.PRICE_PRODUCT_IN_ALERT), 'Price product not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

