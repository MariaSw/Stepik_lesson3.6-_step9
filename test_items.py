import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
class TestBookStore():
    def test_button_presence(self, browser, link):
        browser.implicitly_wait(5)
        browser.get(f"{link}")
        try:
            browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        except NoSuchElementException:
            assert False, "Add to card Button is absent"

