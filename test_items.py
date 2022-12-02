import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        


def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button,'Кнопки на странице нет'
    
