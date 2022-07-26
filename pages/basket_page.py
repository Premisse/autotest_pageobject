from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):

    def no_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_IN_CART), "There are items in cart"

    def no_items_in_cart_message(self):
        assert self.is_element_present(*CartPageLocators.ITEMS_IN_CART_MESSAGE), "There is no message about empty cart"


