from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']")


class BasketPageLocators:
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']/p[text()]")
