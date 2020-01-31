from selenium import webdriver
import pytest


class TestAddCartPage():

    def test_add_to_cart_button(self, browser):
        button = browser.find_element_by_xpath(
            "//button[contains(@class, 'btn-add-to-basket')]")
        assert button.get_attribute('type') == 'submit', "It's not the Submit button "
