from hmw_saucedemo_test import Test_Saucedemocom
testClass = Test_Saucedemocom()

#The test of displaying this text as a warning message 
#when username and password fields are left blank: 'Epic sadface: Username is required.'
testClass.empty_username_password_login_test()

#The test of displaying 'Epic sadface: Password is required' as a warning message when 
#only the password field is left blank.
testClass.empty_password_login_test()

#The test of displaying the message 'Epic sadface: Sorry, this user has been locked out.' 
#when the username 'locked_out_user' and the password 'secret_sauce' are submitted.
testClass.exist_userName_password_login()

#When the username 'standard_user' and the password 'secret_sauce' are submitted, the user should be redirected to the '/inventory.html' page. After logging in,
#the user should see a total of '6' products.
testClass.test_successful_login_and_product_display()