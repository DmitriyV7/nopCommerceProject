import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login ***********")
        self.logger.info("*************** Started Home page title test ***********")
        self.driver=setup
        self.logger.info("*************** Opening URL ***********")
        #self.driver=webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.logger.info("*************** Home page title test passed ***********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleT.png")
            self.driver.close()
            assert True
        else:
            self.logger.error("*************** Home page title test failed ***********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitleF.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Started Login test ***********")
        self.driver=setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.driver.save_screenshot(".\\Screenshots\\" + "user.png")
        self.lp.setPassword(self.password)
        self.driver.save_screenshot(".\\Screenshots\\" + "password.png")
        self.lp.clickLogin()

        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("*************** Login test passed ***********")
            self.driver.close()
            assert True
        else:
            self.logger.error("*************** Login test failed ***********")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False


#pytest -v -s testCases\test_Login.py

#pytest -v -s testCases\test_Login.py --browser chrome
#pytest -v -s testCases\test_Login.py --browser firefox

#pytest -v -s -n=2 testCases\test_Login.py --browser chrome
#pytest -v -s -n=2 testCases\test_Login.py --browser firefox

#pytest -v -s -n=2 --html=Reports\report.html testCases\test_Login.py --browser chrome































