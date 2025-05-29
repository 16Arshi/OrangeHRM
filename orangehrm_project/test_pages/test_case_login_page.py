import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from base_pages.test_login_page import login_Page
from test_pages.conftest import setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class TestLogin01:
    login_url = Read_Config.get_login_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger=Log_Maker.log_gen()

    @pytest.mark.sanity
    def test_verification_of_title(self,setup):
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
    def test_Verification_of_Valid_login(self, setup):
        self.logger.info("*******test verication of valid login is successfull******")
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_admin = login_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()

        wait = WebDriverWait(self.driver, 10)
        dashboard_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[contains(@class, 'oxd-topbar-header-breadcrumb-module')]")
            )
        )
        actual_dashboard_text = dashboard_element.text
        expected_dashboard_text = "Dashboard"

        if actual_dashboard_text != expected_dashboard_text:
            setup.save_screenshot(".\\screenshots\\valid_verification_failed.png")

        self.driver.close()
        assert actual_dashboard_text == expected_dashboard_text

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Verification_of_invalid_credentials(self, setup):
        self.logger.info("*******test verication of invalid credentials is successfull******")
        self.driver = setup
        self.driver.get(self.login_url)
        self.login_admin = login_Page(self.driver)
        self.login_admin.enter_username(self.invalid_username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()

        wait = WebDriverWait(self.driver, 10)
        error_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
            )
        )
        actual_invalid_text = error_element.text
        expected_invalid_text = "Invalid credentials"

        if actual_invalid_text != expected_invalid_text:
            self.driver.save_screenshot(f"invalid_login_failed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

        self.driver.close()
        assert actual_invalid_text == expected_invalid_text
