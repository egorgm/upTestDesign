from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 

    def go_to_product_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 
    
    def click_on_add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
        
    def compare_expected_and_actual_price(self):
        assert (self.browser.find_element(*ProductPageLocators.PRICE)).text == (self.browser.find_element(*ProductPageLocators.COMPLETE_PRICE)).text, "The expected price does not match the actual."
    
    def compare_expected_and_actual_book(self):
        assert (self.browser.find_element(*ProductPageLocators.NAME_BOOK)).text == (self.browser.find_element(*ProductPageLocators.COMPLETE_NAME_BOOK)).text, "The expected book name does not match the actual."
            