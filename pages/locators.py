from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]/p")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/h1")
    PRODUCT_IN_CART_NAME = (By.XPATH, "//div[contains(@class,'alertinner')]/strong")
    PRODUCT_IN_CART_PRICE = (By.XPATH, "//div[contains(@class,'alertinner')]/p/strong")
