import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, time
from base_pages.test_login_page import login_Page
from test_pages.conftest import setup
from utilities import excel_utilis
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
import time

class TestLogin02:
    login_url = Read_Config.get_login_url()
    logger=Log_Maker.log_gen()
    path=".//test_data//orangehrm.xlsx"
    status_list=[]

    @pytest.mark.sanity
    def test_verification_of_title_data_driven(self,setup):
        self.logger.info("*******test verication of title is successfull******")
        self.driver =setup
        self.driver.get(self.login_url)
        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if actual_title != expected_title:
            setup.save_screenshot(".\\screenshots\\title_verification_failed.png")

        self.driver.close()
        assert actual_title == expected_title

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Verification_of_Valid_login_data_driven(self, setup):
        self.logger.info("*******test verication of valid login is successfull******")
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_admin = login_Page(self.driver)


        self.rows=excel_utilis.get_row_count(self.path,"Sheet1")
        print("num of rows",self.rows)

        for r in range(2,self.rows+1):
            self.username=excel_utilis.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utilis.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utilis.read_data(self.path, "Sheet1", r, 3)
            self.login_admin.enter_username(self.username)
            self.login_admin.enter_password(self.password)
            self.login_admin.click_login()
            time.sleep(3)

            wait = WebDriverWait(self.driver, 10)
            dashboard_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[contains(@class, 'oxd-topbar-header-breadcrumb-module')]")
            )
                )
        actual_dashboard_text = dashboard_element.text
        expected_dashboard_text = "Dashboard"

        if actual_dashboard_text == expected_dashboard_text:
            if self.exp_login=="Yes":
                self.logger.info("passed")
                self.status_list.append("pass")

            elif  self.exp_login=="no":
                self.logger.info("failed")
                self.status_list.append("fail")

        elif  actual_dashboard_text != expected_dashboard_text:
            if self.exp_login == "Yes":
                self.logger.info("failed")
                self.status_list.append("fail")

            elif self.exp_login == "no":
                self.logger.info("passed")
                self.status_list.append("pass")

        print("Staus list is",self.status_list)

        if "fail" in self.status_list:
            self.logger.info("data is failed")
            assert False

        else:
            self.logger.info("data is passed")
            assert True