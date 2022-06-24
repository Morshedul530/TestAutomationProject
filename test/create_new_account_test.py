import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.create_new_account import CreateAccountPage
from pages.sign_in import SignIn
from pages.signup_page import SignUp


class CreateAccountTest(unittest.TestCase):
    def test_create_account(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        signin = SignIn(driver)
        signin.signin_page()

        signup = SignUp(driver)
        signup.signup_page("shuvo4845@gmail.com")

        cap = CreateAccountPage(driver)
        cap.create_account("Mr.", "Shuvo", "01746604763", "BITM", "Mirpur-12", "Dhaka", "12345",
                          "All information is valid", "01571231339", "01746604763", "Dinajpur")

        # Screenshot
        driver.save_screenshot("D:\\Project\Assignment\\TestAutomationProject\\screenshot\\Create_New_Account.png")

        driver.close()
