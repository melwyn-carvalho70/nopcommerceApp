import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # calling the method from the LogGeneration class and saving in logger.

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("***** Test_005_SearchCustomerByName *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Search Customer Test *****")
        self.addcust = AddCustomer(self.driver)  # creating an object for the AddCustomer page object
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("***** Searching Customer by Name *****")
        self.searchcust = SearchCustomer(self.driver)  # creating an object for the SearchCustomer page object
        time.sleep(3)
        self.searchcust.setSearchFirstName('Victoria')
        self.searchcust.setSearchLastName('Terces')

        self.searchcust.clickSearch()
        time.sleep(3)

        status = self.searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("***** Test_005_SearchCustomerByName Finished *****")
        self.driver.close()





