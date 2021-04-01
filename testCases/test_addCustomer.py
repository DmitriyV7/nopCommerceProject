import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("*************** Started Test_AddCustomer test ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login succesful*************")

        self.logger.info("***********Starting Add Customer Test*************")

        self.adcust = AddCustomer(self.driver)
        self.adcust.clickOnCustomersMenu()
        time.sleep(2)
        self.adcust.clickOnCustomersMenuItem()

        self.adcust.clickOnAddnew()
        #time.sleep(3)

        self.logger.info("***************Providing customer info************")

        self.email = random_generator() +"@gmail.com"
        self.adcust.setEmail(self.email)
        self.adcust.setPassword("test123")
        self.adcust.setCustomerRoles("Guests")
        self.adcust.setFirstName("Eric")
        self.adcust.setLastName("Popopopko")
        self.adcust.setGender("Female")
        self.adcust.setDob("08/09/2000")
        self.adcust.setCompanyName("New Tester Chicago Land")
        self.adcust.setTax("Yes")
        self.adcust.setNewsLetter("Test store 2") #Test store 2
        self.adcust.setManagerOfVendor("Vendor 2")
        self.adcust.setAdminComment("If you can see this...I did it")
        self.adcust.clickOnSave()

        self.logger.info("***********Saving customer info**********")

        self.logger.info("***********Add customer validation started**********")

        self.msg=self.driver.find_element_by_tag_name("body").text

        #print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("********Add customer Test Passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCustomer_scr.png")
            self.logger.error("********Add customer Test Failed*********")
            assert False
        time.sleep(4)

        self.driver.close()
        self.logger.info("*********************Test Passed***************************")



def random_generator(size=10,chars=string.ascii_uppercase + string.digits):  # random generator method
    return ''.join(random.choice(chars) for x in range(size))



#pytest -s -v -n=2 testCases\test_addCustomer.py  --browser chrome
#pytest -s -v -n=2 -m "sanity" --capture=tee-sys --html=./Reports/reporttest.html testCases/ --browser chrome
#pytest -s -v -n=2 -m "regression" --capture=tee-sys --html=./Reports/reporttest.html testCases/ --browser chrome
#pytest -s -v -n=2 -m "sanity and regression" --capture=tee-sys --html=./Reports/reporttest.html testCases/ --browser chrome
#pytest -s -v -n=2 -m "sanity or regression" --capture=tee-sys --html=./Reports/reporttest.html testCases/ --browser chrome
#+ string.digits




























