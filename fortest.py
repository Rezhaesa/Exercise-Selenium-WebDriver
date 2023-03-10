import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestSHOPPINGCART(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

#shoppingcart_checkout
    def test_success_shoppingcart_checkout(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rezha.cacahrian@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "login-button").click()

        driver.find_element(By.LINK_TEXT, "Books").click()
        respon = driver.find_element(By.CLASS_NAME, "page-title").text
        self.assertIn("Books", respon)        
        success_shoppingcart_book_url = driver.current_url
        self.assertEqual(success_shoppingcart_book_url, "https://demowebshop.tricentis.com/books")
        driver.find_element(By.CLASS_NAME, "product-box-add-to-cart-button").click()
        respon = driver.find_element(By.ID, "dialog-notifications-success")

        driver.find_element(By.TAG_NAME, "a").click()
        success_shoppingcart_book_url = driver.current_url
        self.assertEqual(success_shoppingcart_book_url, "https://demowebshop.tricentis.com/")

        driver.get("https://demowebshop.tricentis.com/cart")
        driver.find_element(By.ID, "CountryId").click()
        driver.find_element(By.CSS_SELECTOR, "div.inputs").click()  
        driver.find_element(By.CLASS_NAME, "zip-input").send_keys("123ZIP456")
        driver.find_element(By.CLASS_NAME, "qty-input").send_keys("10")
        driver.find_element(By.CLASS_NAME, "estimate-shipping-button").click()
        respon = driver.find_element(By.CLASS_NAME, "option-description").text
        self.assertIn("Compared to other shipping methods, like by flight or over seas, ground shipping is carried out closer to the earth", respon)
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.NAME, "removefromcart").click()
        driver.find_element(By.ID, "checkout").click()
        success_shoppingcart_book_url = driver.current_url
        self.assertEqual(success_shoppingcart_book_url, "https://demowebshop.tricentis.com/onepagecheckout")
        
        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'new-address-next-step-button')))
        respon = driver.find_element(By.TAG_NAME, "Shipping address")

if __name__ == '__main__':
    unittest.main()