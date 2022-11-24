import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # calling the method from the LogGeneration class and saving in logger

    @pytest.mark.sanity

    def test_addCustomer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Add Customer Test *****")
        self.addcust = AddCustomer(self.driver)  # creating an object for the AddCustomer page object
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing customer details *****")

        self.email = random_generator() + "@gmail.com"  # random_generator function is below
        self.addcust.setEmail(self.email)

        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Melwyn")
        self.addcust.setLastName("Simon")
        self.addcust.setGender("Male")
        self.addcust.setDoB("1/1/1995")  # mm/dd/yyyy
        self.addcust.setCompanyNmae("MSC")

        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminComment("Test entry")

        self.addcust.clickOnSave()

        self.logger.info("***** Saving customer information *****")

        self.logger.info("***** Add customer validation started *****")

        # capture the success text
        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***** Add Customer Test passed *****")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_addCustomer.png")
            self.logger.error("***** Add Customer test failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending Add Customer Test *****")
        self.logger.info("***** ****** *****")


# function to randomly generate the email
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
