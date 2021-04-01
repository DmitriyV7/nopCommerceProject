from selenium.webdriver.support.ui import Select
import time



class AddCustomer:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_by_id = "Email"
    txtPassword_by_id = "Password"
    txtFirstName_by_id = "FirstName"
    txtLastName_by_id = "LastName"
    rbMGender_by_id = "Gender_Male"
    rbFGender_by_id = "Gender_Female"
    txtDob_by_id = "DateOfBirth"
    txtCompanyName_by_id = "Company"
    rbTax_by_id = "IsTaxExempt"
    #newsletter_by_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']"
    drpNewsletter_by_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    news_yourstorename_by_xpath = "//li[normalize-space()='Your store name']"
    news_teststore_by_xpath = "//li[normalize-space()='Test store 2']"
    txtcustomerRoles_by_xpath ="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listemAdministrators_xpath = "// span[normalize - space() = 'Administrators']"
    listemForumModerators_xpath = "// span[normalize - space() = 'Forum Moderators']"
    listemGuests_xpath = "//li[normalize-space()='Guests']"
    listemRegistered_xpath = "//li[normalize-space()='Registered']"
    listemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgOfVendor_by_id = "VendorId"
    txtAdminComment_by_id = "AdminComment"
    btnSave_by_name = "save"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_by_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtPassword_by_id).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element_by_id(self.txtFirstName_by_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_id(self.txtLastName_by_id).send_keys(lastname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_id(self.rbMGender_by_id).click()
        elif gender=="Female":
            self.driver.find_element_by_id(self.rbFGender_by_id).click()
        else:
            self.driver.find_element_by_id(self.rbMGender_by_id).click()

    def setDob(self,dob):
        self.driver.find_element_by_id(self.txtDob_by_id).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_id(self.txtCompanyName_by_id).send_keys(comname)

    def setTax(self, tax):
        if tax=="Yes":
            self.driver.find_element_by_id(self.rbTax_by_id).click()
        else:
            print("Not Tax Payer")


    def setNewsLetter(self, newsvalue):
        self.driver.find_element_by_xpath(self.drpNewsletter_by_xpath).click()
        time.sleep(3)
        #drpNews=Select(self.driver.find_element_by_xpath(self.newsletter_by_xpath))
        if newsvalue=="Your store name":
            self.listnew=self.driver.find_element_by_xpath(self.news_yourstorename_by_xpath).click()
        elif newsvalue=="Test store 2":
            self.listnew=self.driver.find_element_by_xpath(self.news_teststore_by_xpath).click()
        else:
            self.listnew=self.driver.find_element_by_xpath(self.news_teststore_by_xpath).click()


    def  setCustomerRoles(self,role):
        #self.driver.find_element_by_xpath("//span[@title='delete']").click()
        self.driver.find_element_by_xpath(self.txtcustomerRoles_by_xpath).click()
        time.sleep(5)
        if role=="Registered":
            self.listitem=self.driver.find_element_by_xpath(self.listemRegistered_xpath)
        elif role=="Administrators":
            self.listitem=self.driver.find_element_by_xpath(self.listemAdministrators_xpath)
        elif role=="Guests":
            time.sleep(5)
            #//span[@title='delete']
            #self.driver.find_element_by_xpath("//span[@title='delete']").click()
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            #self.driver.find_element_by_xpath(self.txtcustomerRoles_by_xpath).click()
            self.listitem=self.driver.find_element_by_xpath(self.listemGuests_xpath).click()
        elif role=="Registered":
            self.listitem=self.driver.find_element_by_xpath(self.listemRegistered_xpath).click()
        elif role=="Vendors":
            self.listitem=self.driver.find_element_by_xpath(self.listemVendors_xpath).click()
        else:
            self.listitem=self.driver.find_element_by_xpath(self.listemGuests_xpath).click()
            #time.sleep(3)
            #self.listitem.click()
            #self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self, venvalue):
        drpMang=Select(self.driver.find_element_by_id(self.drpmgOfVendor_by_id))
        drpMang.select_by_visible_text(venvalue)

    def setAdminComment(self, comment):
        self.driver.find_element_by_id(self.txtAdminComment_by_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_name(self.btnSave_by_name).click()












































