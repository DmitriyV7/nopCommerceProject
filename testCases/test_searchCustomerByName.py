import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_005:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************************Search Customer By Email_005****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************Login successful *****************")

        self.logger.info("*************Starting Search Customer By Name ******************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*****************Searching customer by emailID**********************")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName("Lindgren")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.serchCustomerByName("Brenda Lindgren")
        self.driver.close()
        assert True==status
        self.logger.info("*******************TC SearchCustomerByName_005 Finished******************")




#pytest -s -v -n=2 testCases\test_searchCustomerByName.py --browser chrome



#pytest -s -v -n=2  --capture=tee-sys --html=Reports\report2.html testCases\ --browser chrome





























































