import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

from pages.sign_in import SignIn
from pages.login import LoginPage


class Login_test(unittest.TestCase):

    def test_login(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseURL)
        time.sleep(2)

        signin = SignIn(driver)
        signin.signin_page()

        lp = LoginPage(driver)
        lp.login_page("mshuvo530@gmail.com", "01746604763")
        time.sleep(3)

        driver.close()
