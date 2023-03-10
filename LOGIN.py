import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLOGIN(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

#login_page
    def test_success_login_page(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()

        respon = driver.find_element(By.CLASS_NAME, "page-title").text
        self.assertIn("Welcome, Please Sign In!", respon)
        success_login_page_url = driver.current_url
        self.assertEqual(success_login_page_url, "https://demowebshop.tricentis.com/login")

#success_login
    def test_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "login-button").click()

#success_login_with_rememberme
    def test_success_login_with_rememberme(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.CLASS_NAME, "login-button").click()

#failed_login_empty
    def test_login_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CLASS_NAME, "login-button").click()

        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", respon)
        failed_login_url = driver.current_url
        self.assertEqual(failed_login_url, "https://demowebshop.tricentis.com/login")


#failed_login_email_empty
    def test_login_email_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "login-button").click()

        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("No customer account found", respon)
        failed_login_url = driver.current_url
        self.assertEqual(failed_login_url, "https://demowebshop.tricentis.com/login")

#failed_login_password_empty
    def test_login_password_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CLASS_NAME, "login-button").click()

        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect", respon)
        failed_login_url = driver.current_url
        self.assertEqual(failed_login_url, "https://demowebshop.tricentis.com/login")

#failed_login_password_incorrect
    def test_login_password_incorrect(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("1234567")
        driver.find_element(By.CLASS_NAME, "login-button").click()

        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect", respon)
        failed_login_url = driver.current_url
        self.assertEqual(failed_login_url, "https://demowebshop.tricentis.com/login")

if __name__ == '__main__':
    unittest.main()