import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.EditCustomer import EditCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_006_EditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # calling the method from the LogGeneration class and saving in logger

    @pytest.mark.sanity
    def test_editCustomer(self, setup):
        self.logger.info("***** Test_006_EditCustomer *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Edit Customer Test *****")
        self.addcust = AddCustomer(self.driver)  # creating an object for the AddCustomer page object
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("***** Editing Customer Info *****")
        self.editcust = EditCustomer(self.driver)
        time.sleep(3)
        self.editcust.clickOnEdit()
        time.sleep(3)

        self.editcust.editGender('Female')
        self.editcust.EditcompanyName('nopcommerceLTD')
        self.editcust.CheckTaxExempt()
        self.editcust.addAdmincomment('Gender set to Female, company name added, tax exempted')
        time.sleep(2)

        self.editcust.clickOnSaveButton()
        self.logger.info("***** Saving edited customer information *****")

        self.logger.info("***** edit customer validation started *****")

        # capture the success text
        self.success_msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'The customer has been updated successfully.' in self.success_msg:
            assert True == True
            self.logger.info("***** Edit Customer Test passed *****")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_editCustomer.png")
            self.logger.error("***** Edit Customer test failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending Edit Customer Test *****")
        self.logger.info("***** ****** *****")
