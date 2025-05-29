from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout
        self.username_xpath = "//input[@name='username']"
        self.password_xpath = "//input[@name='password']"
        self.login_btn_xpath = "//button[@type='submit']"
        self.logout_xpath="//a[normalize-space()='Logout']"

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_xpath)))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_xpath)))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_btn_xpath)))
        login_btn.click()
