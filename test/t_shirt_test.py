import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

from pages.login import LoginPage
from pages.sign_in import SignIn
from pages.t_shirt_page import TShirtPage
from pages.payment_process_page import PaymentProcessPage


class Tshirt_SelectionTest(unittest.TestCase):

    def test_tshirt_selection(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_page()

        lp = LoginPage(driver)
        lp.login_page("mshuvo530@gmail.com", "01746604763")
        time.sleep(3)

        tsp = TShirtPage(driver)
        tsp.t_shirt_page()
        time.sleep(3)

        ppp = PaymentProcessPage(driver)
        ppp.payment_process()
        time.sleep(3)
