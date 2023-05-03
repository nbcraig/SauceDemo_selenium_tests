from pages.common_operations import CommonOps
from selenium.webdriver.common.by import By

class LoginPage(CommonOps):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_message = (By.TAG_NAME, 'h3')
    title_element = (By.CLASS_NAME, 'title')

    def login(self, username, password):
        self.wait_for(self.username_field).send_keys(username)
        self.get_element(self.password_field).send_keys(password)
        self.get_element(self.login_button).click()

    def check_successful_login(self):
        self.get_element(self.title_element)

    def check_error_message(self):
        self.get_element(self.error_message)