from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_correct_name(self):
        actual_name = self.browser.find_element(By.XPATH, "//div[@class='alertinner ']/strong").text
        expected_name = self.browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1").text
        assert expected_name == actual_name

    def should_be_correct_price(self):
        expected_name = self.browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']").text
        actual_name = self.browser.find_element(By.XPATH, "//div[@class='alertinner ']/p/strong").text
        return expected_name == actual_name
