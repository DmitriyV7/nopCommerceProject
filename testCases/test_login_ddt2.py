import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_003_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("*************** Started Test_003_DDT_Login test ***********")
        self.driver=setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)


        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print('Number of rows....', self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path, 'Sheet1', r,1) # user name
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2) # password
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3) # expected



            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title: # Login Success
                if self.exp=='Pass':
                    self.logger.info('*****Passed*****')
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                    assert True
                elif self.exp=='Fail':
                    self.logger.info('*****Failed*****')
                    self.lp.clickLogout()
                    lst_status.append("Failed")
                    assert False

            elif act_title!=exp_title: # Login is NOT Succesful
                if self.exp=='Pass':
                    self.logger.info('*****Failed*****')
                    lst_status.append("Failed")

                elif self.exp=='Fail':
                    self.logger.info('*****Passed*****')
                    lst_status.append("Pass")

            print(lst_status)


        if'Fail' not in lst_status:
            self.logger.info("*****DDT Login test Passed*****")
            self.driver.close()
            assert True
        else:
            self.logger.error("*****DDT Login test Failed*****")
            self.driver.close()
            assert False
        self.logger.info("*************Finished Test_003_DDT_Login**************")
        self.logger.info("**************** Completed  TC_LoginDDT_003 ************* ")




#pytest -v -s testCases\test_login_ddt2.py

#pytest -v -s testCases\test_login_ddt2.py --browser chrome
#pytest -v -s testCases\test_login_ddt2.py --browser firefox

#pytest -v -s -n=2 testCases\test_login_ddt2.py --browser chrome
#pytest -v -s -n=2 testCases\test_login_ddt2.py --browser firefox



#testCases/test_login_ddt2.py





























