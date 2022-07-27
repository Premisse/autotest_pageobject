from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, "//a[contains(@href,'basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_USER_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]/p")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_IN_CART_NAME = (By.XPATH, "//div[contains(@class,'alertinner')]/strong")
    PRODUCT_IN_CART_PRICE = (By.XPATH, "//div[contains(@class,'alertinner')]/p/strong")

class CartPageLocators():
    ITEMS_IN_CART = (By.CSS_SELECTOR, ".basket-items")
    ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
