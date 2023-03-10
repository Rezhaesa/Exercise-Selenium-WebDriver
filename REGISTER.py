import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestREGISTER(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

#register_page
    def test_success_register_page(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()

        respon = driver.find_element(By.CLASS_NAME, "page-title").text
        self.assertIn("Register", respon)
        success_register_page_url = driver.current_url
        self.assertEqual(success_register_page_url, "https://demowebshop.tricentis.com/register")

#failed_register_email_already_exist
    def test_a_failed_register_email_already_exist(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register/")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Rezha")
        driver.find_element(By.ID, "LastName").send_keys("Sachrian")

        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
        driver.find_element(By.ID, "register-button").click()

        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertIn("The specified email already exists", respon)
        failed_register_url = driver.current_url
        self.assertEqual(failed_register_url, "https://demowebshop.tricentis.com/register/")


#success_register
    def test_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register/")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Rezha")
        driver.find_element(By.ID, "LastName").send_keys("Sachrian")

        driver.find_element(By.ID, "Email").send_keys("rzhsch@gmcailab.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
        driver.find_element(By.ID, "register-button").click()

        respon = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn("Your registration completed", respon)
        success_register_url = driver.current_url
        self.assertEqual(success_register_url, "https://demowebshop.tricentis.com/registerresult/1")

#continue_success_register
    def test_continue_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/registerresult/1")
        driver.find_element(By.CLASS_NAME, "buttons").click()

#failed_register_gender_empty
    def test_a_failed_register_gender_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register/")
        driver.find_element(By.ID, "FirstName").send_keys("Rezha")
        driver.find_element(By.ID, "LastName").send_keys("Sachrian")

        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmailll.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
        driver.find_element(By.ID, "register-button").click()
    
#FAILURE_RESPON
        respon = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn("Your registration not completed", respon)
        failed_register_url = driver.current_url
        self.assertEqual(failed_register_url, "https://demowebshop.tricentis.com/registerresult/1")

#failed_register_email_empty
    def test_a_failed_register_email_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register/")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Rezha")
        driver.find_element(By.ID, "LastName").send_keys("Sachrian")

        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
        driver.find_element(By.ID, "register-button").click()
    
        respon = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Email is required.", respon)
        failed_register_url = driver.current_url
        self.assertEqual(failed_register_url, "https://demowebshop.tricentis.com/register/")

#failed_register_password_not_match
    def test_a_failed_register_password_not_match(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register/")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Rezha")
        driver.find_element(By.ID, "LastName").send_keys("Sachrian")

        driver.find_element(By.ID, "Email").send_keys("rzhschrn@gmailll.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("1234567")
        driver.find_element(By.ID, "register-button").click()
               
        respon = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("The password and confirmation password do not match.", respon)
        failed_register_url = driver.current_url
        self.assertEqual(failed_register_url, "https://demowebshop.tricentis.com/register/")

   
    #def test_success_register(self):
        #driver = self.browser
        #driver.get("https://demowebshop.tricentis.com/register/")
        #driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #driver.find_element(By.ID, "login-button").click()
        #data = driver.find_element(By.CSS_SELECTOR, ".error-message-container.error").text
        #self.assertIn("Epic sadface: Sorry, this user has been locked out.", data)

if __name__ == '__main__':
    unittest.main()