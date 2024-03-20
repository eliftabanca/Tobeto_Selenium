from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test_Saucedemocom:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        
    def empty_username_password_login_test(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(3)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMassage = self.driver.find_element(By.ID, "login_button_container")
        print(errorMassage.text)
        test_result = errorMassage.text == "Epic sadface: Username is required"
        print(f"Test Resuld is {test_result}")
        sleep(2)
    
    def empty_password_login_test(self): 
        self.driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMassage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMassage.text)
        test_result = errorMassage.text == "Epic sadface: Password is required"
        print(f"Test Resuld is {test_result}")
        sleep(2)
        
    
    def exist_userName_password_login(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userNameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMassage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Resuld is {testResult}")
        sleep(2)
        
        
    def test_successful_login_and_product_display(self):
         self.driver.get("https://www.saucedemo.com/")
         sleep(3)
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

         if current_url == expectedUrl:
              print("Expected URL is visible.")
         else:
          print("Expected URL is not visible.") 
          
          
        
         products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")
         time.sleep(10)
         currentProductsNumber = len(products)
         
         if  currentProductsNumber == 6:
          print("Yes! There are 6 products.")
         else:
          print("NO! There are not 6 products.")
         
         
        

    
        
        



