from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
