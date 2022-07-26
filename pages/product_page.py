from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def product_info_should_be_the_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_NAME).text
        assert product_price == product_price_in_cart, "Product price is not the same"
        assert product_name == product_name_in_cart, "Product name is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

