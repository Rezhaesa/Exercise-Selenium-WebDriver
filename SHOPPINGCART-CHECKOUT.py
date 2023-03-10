import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestSHOPPINGCART(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

def test_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("rezha.cacahrian@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "login-button").click()

#shoppingcart_empty
    def test_success_shoppingcart_empty(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-cart").click()
        respon = driver.find_element(By.CLASS_NAME, "order-summary-content").text
        self.assertIn("Your Shopping Cart is empty!", respon)
        success_shoppingcart_page_url = driver.current_url
        self.assertEqual(success_shoppingcart_page_url, "https://demowebshop.tricentis.com/cart")

#shoppingcart_entry
    def test_success_shoppingcart_page(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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

#shoppingcart_add_discount
    def test_success_shoppingcart_discount(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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
        driver.find_element(By.CLASS_NAME, "discount-coupon-code").send_keys("123code456")
        driver.find_element(By.CLASS_NAME, "apply-discount-coupon-code-button").click()
        success_shoppingcart_book_url = driver.current_url
        self.assertEqual(success_shoppingcart_book_url, "https://demowebshop.tricentis.com/cart")
        respon = driver.find_element(By.CLASS_NAME, "message").text
        self.assertIn("The coupon code you entered couldn't be applied to your order", respon) 

#shoppingcart_add_giftcards
    def test_success_shoppingcart_giftcards(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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
        driver.find_element(By.CLASS_NAME, "gift-card-coupon-code").send_keys("123codegift456")
        driver.find_element(By.CLASS_NAME, "apply-gift-card-coupon-code-button").click()
        success_shoppingcart_book_url = driver.current_url
        self.assertEqual(success_shoppingcart_book_url, "https://demowebshop.tricentis.com/cart")
        respon = driver.find_element(By.CLASS_NAME, "message").text
        self.assertIn("The coupon code you entered couldn't be applied to your order", respon) 

#shoppingcart_add_shipping
    def test_success_shoppingcart_add_shipping(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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
        driver.find_element(By.CLASS_NAME, "estimate-shipping-button").click()
        respon = driver.find_element(By.CLASS_NAME, "option-description").text
        self.assertIn("Compared to other shipping methods, like by flight or over seas, ground shipping is carried out closer to the earth", respon) 

#shoppingcart_checkout_failed
    def test_success_shoppingcart_checkout_failed(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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
        driver.find_element(By.CLASS_NAME, "estimate-shipping-button").click()
        respon = driver.find_element(By.CLASS_NAME, "option-description").text
        self.assertIn("Compared to other shipping methods, like by flight or over seas, ground shipping is carried out closer to the earth", respon) 
        driver.find_element(By.ID, "checkout").click()
        respon = driver.find_element(By.CLASS_NAME, "ui-dialog-content").text
        self.assertIn("Please accept the terms of service before the next step.", respon)

#shoppingcart_checkout
    def test_success_shoppingcart_checkout(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
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

if __name__ == '__main__':
    unittest.main()