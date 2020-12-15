from selenium import webdriver
import time
import unittest

# for running in cdm *calling POMdemo problem
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POMdemo.Pages.LoginPage import LoginPage
from POMdemo.Pages.HomePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Pim/PycharmProjects/test/WebDriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()

        # self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        # self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        # self.driver.find_element_by_id('btnLogin').click()
        #
        # self.driver.find_element_by_id('welcome').click()
        # self.driver.find_element_by_link_text('Logout').click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Pim/PycharmProjects/test/POMdemo/report'))