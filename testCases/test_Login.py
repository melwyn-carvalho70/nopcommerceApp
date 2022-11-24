import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()   # calling the method from the LogGeneration class and saving in logger

    @pytest.mark.sanity
    @pytest.mark.regression
    # verify title
    def test_homePageTitle(self, setup):

        self.logger.info("*****Test_001_Login*****")
        self.logger.info("*****Verifying the Homepage Title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title


        if actual_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("*****Homepage title test is passed*****")

        else:
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\nopcommerceApp\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****Homepage title test is failed*****")
            assert False
    # -----------------------------------------------------------------------------------------------------------------------


    @pytest.mark.regression
    # Perform login
    def test_login(self, setup):
        self.logger.info("*****Test_001_Login*****")
        self.logger.info("*****Verifying the Login Title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create an object of LoginPage to access the methods
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()

        actual_title = self.driver.title

        if actual_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("*****Login title test is passed*****")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("*****Login title test is failed*****")
            assert False


