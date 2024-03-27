
import time
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #hangi şarta baglı olarak bekeleyecegini
from selenium.webdriver.common.action_chains import ActionChains

from pathlib import Path
from datetime import date

class Test_Saucedemocom:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")
     
    def teardown_method(self):
        self.driver.quit()
    
    def test_logout(self):
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click() 
        burger_menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_button.click()   
        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
        self.driver.execute_script("arguments[0].click();", logout_button)

      
        
        current_url = self.driver.current_url
        excepted_url = "https://www.saucedemo.com/"
        assert excepted_url == current_url
        
        
        
    def test_basket_product_number(self):   
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click() 
        addButton = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        addButton.click()
        sleep(5)
        current_basket_locater = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        expected_basket_locetor = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert expected_basket_locetor.is_displayed
     
    def waitForElementVisiable(self,locator,timeout=5):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))   
            
    def test_add_basket(self):
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisiable(((By.ID,"user-name")),10)
        userNameInput.send_keys("standard_user")
       
        self.waitForElementVisiable(((By.ID,"password")),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
      
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click() 
        addButton = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        addButton.click()
        expected_button = self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
        assert expected_button.is_displayed()   
          
    def test_test_empty_username_password_login(self):
       
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMassage = self.driver.find_element(By.ID, "login_button_container")
        test_result = "Epic sadface: Username is required"
        assert test_result == errorMassage.text
        sleep(2)
    

    def test_emptyPassword_login_test(self): 
           
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMassage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = "Epic sadface: Password is required"
        assert errorMassage.text == test_result
        sleep(2)
        
   
    def test_exist_userName_password_login(self):
        
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("locked_out_user")
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMassage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = "Epic sadface: Sorry, this user has been locked out."
        assert errorMassage.text == testResult
        
    def test_successful_login_and_product_display(self):
         
         userNameInput = self.driver.find_element(By.ID, "user-name")
         userNameInput.send_keys("standard_user")
         sleep(2)
         passwordInput = self.driver.find_element(By.ID, "password")
         passwordInput.send_keys("secret_sauce")
         sleep(2)
         loginButton = self.driver.find_element(By.ID, "login-button")
         loginButton.click()
    
         expectedUrl = "https://www.saucedemo.com/inventory.html"
         
         current_url = self.driver.current_url
         assert current_url == expectedUrl
          
         products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")
         time.sleep(10)
         currentProductsNumber = len(products)
         
         assert currentProductsNumber == 6

    
    @pytest.mark.parametrize("username, password", [("yalnis_isim1", "secret_sauce"),("yalnis_isim2", "jhnjh"),("yalnis_isim3", "nknk")])  
    def test_invalid_login(self, username, password):
     userNameInput = self.driver.find_element(By.ID, "user-name")
     userNameInput.send_keys(username)
     passwordInput = self.driver.find_element(By.ID, "password")
     passwordInput.send_keys(password)
     loginButton = self.driver.find_element(By.ID, "login-button")
     loginButton.click()
     
     
   
    



