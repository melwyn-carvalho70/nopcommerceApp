import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    excelPath = ReadConfig.getExcelPath()
    logger = LogGen.loggen()   # calling the method from the LogGeneration class and saving in logger


    @pytest.mark.regression
    # Perform login
    def test_login_ddt(self,setup):
        self.logger.info("****** Test_002_DDT_Login ******")
        self.logger.info("**** Verifying Login DDT ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create an object of LoginPage to access the methods
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.excelPath, "Sheet1")
        print("number of rows:", self.rows)

        list_status = []    # empty list variable

        # for loop to extract data from the Excel sheet
        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.excelPath, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.excelPath, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.excelPath, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            time.sleep(5)
            self.lp.clickLogin()

            actual_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'


            # comparing titles for verification
            if actual_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    list_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif actual_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    list_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DDt passed****")
            self.driver.close()
            assert True

        else:
            self.logger.info("**** Login DDt passed****")
            self.driver.close()
            assert False

        self.logger.info("**** End of Test_002_DDT_Login  ******")
        self.logger.info("**** Test_002_DDT_Login passed ****")