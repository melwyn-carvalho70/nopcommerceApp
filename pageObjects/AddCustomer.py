import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomers_menu_xpath = '//a[@href="#"]//p[contains(text(), "Customers")]'
    lnkCustomers_menuitem_xpath = '//a[@href="/Admin/Customer/List"]//p[contains(text(), " Customers")]'
    btnAddNew_xpath = '/html/body/div[3]/div[1]/form[1]/div/div/a'

    # form on customers page
    txtEmail_id = 'Email'
    txtPassword_id = 'Password'
    txtFirstname_id = 'FirstName'
    txtLastname_id = 'LastName'
    rd_MaleGender_id = 'Gender_Male'
    rd_FemaleGender_id = 'Gender_Female'
    txtDob_id = 'DateOfBirth'
    txtCompanyname_id = 'Company'
    # chkIsTaxExempt_id = 'IsTaxExempt'

    # txtNewsletter_xpath ='//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div/div'
    # lstItemYourSToreName_id = '38e883a2-3d73-466f-bb2f-71e02ceb75de'
    # lstItemTestStore_id = '38e883a2-3d73-466f-bb2f-71e02ceb75de'

    txtCustomerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lstItemAdministrators_id = '6cbbb147-17b4-41df-9c24-360e8a328680'
    lstItemForumModerators_id = '6cbbb147-17b4-41df-9c24-360e8a328680'
    lstItemGuests_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]'
    lstItemRegistered_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    lstItemVendors_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'

    dropdownManagerOfVendor_id = 'VendorId'
    txtAdminComment_id ='AdminComment'

    btnSave_xpath = '//button[@name="save"]'

    def __init__(self, driver):   #constructor
        self.driver = driver

    # -----------------------------------------------------------------

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).clear()
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstname_id).clear()
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rd_MaleGender_id).click()

        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rd_MaleGender_id).click()

        else:
            self.driver.find_element(By.ID, self.rd_MaleGender_id).click()

    def setDoB(self, dob):
        self.driver.find_element(By.ID, self.txtDob_id).clear()
        self.driver.find_element(By.ID, self.txtDob_id).send_keys(dob)

    def setCompanyNmae(self, companyname):
        self.driver.find_element(By.ID, self.txtCompanyname_id).clear()
        self.driver.find_element(By.ID, self.txtCompanyname_id).send_keys(companyname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)

        elif role == 'Administrators':
            self.listItem = self.driver.find_element(By.ID, self.lstItemAdministrators_id)

        elif role == 'Guests':
            # here user can be Registered or Guest
            # First delete the registered selection
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            self.listItem = self.driver.find_element(By.XPATH, self.lstItemGuests_xpath)

        elif role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)

        elif role == 'Vendors':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItemVendors_xpath)

        else:
            self.listItem = self.driver.find_element(By.XPATH, self.lstItemGuests_xpath)

        time.sleep(3)
        # to click
        self.driver.execute_script("arguments[0].click()", self.listItem)


    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.dropdownManagerOfVendor_id))
        drp.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element(By.ID, self.txtAdminComment_id).clear()
        self.driver.find_element(By.ID, self.txtAdminComment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()













































