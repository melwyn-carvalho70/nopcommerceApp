import time
from selenium.webdriver.common.by import By


class EditCustomer:
    btnEditCustomer_xpath = '//*[@id="customers-grid"]/tbody/tr[1]/td[7]/a'
    rdGenderMale_id = 'Gender_Male'
    rdGenderFemale_id = 'Gender_Female'
    txtCompanyName_id = 'Company'
    chkIsTaxExempt_id = 'IsTaxExempt'
    txtAdminComment_id = 'AdminComment'
    btnSave_xpath = '//button[@type="submit" and @name="save"]'

    def __init__(self, driver):  # constructor
        self.driver = driver

    # -----------------------------------------------------------------

    def clickOnEdit(self):
        self.driver.find_element(By.XPATH, self.btnEditCustomer_xpath).click()

    def editGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdGenderMale_id).click()

        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdGenderFemale_id).click()

    def EditcompanyName(self, compname):
        self.driver.find_element(By.ID, self.txtCompanyName_id).clear()
        self.driver.find_element(By.ID, self.txtCompanyName_id).send_keys(compname)

    def CheckTaxExempt(self):
        self.driver.find_element(By.ID, self.chkIsTaxExempt_id).click()

    def addAdmincomment(self, comment):
        self.driver.find_element(By.ID, self.txtAdminComment_id).clear()
        self.driver.find_element(By.ID, self.txtAdminComment_id).send_keys(comment)

    def clickOnSaveButton(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()