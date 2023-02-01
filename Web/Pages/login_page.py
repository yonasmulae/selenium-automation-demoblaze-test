from selenium.webdriver.common.by import By
from Web.Locators.locators_login import login_locator


class Login(login_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()

    def set_user_name(self, username):
        self.driver.find_element(By.XPATH, self.text_box_login_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_login_username_xpath).send_keys(username)

    def set_user_password(self, password):
        self.driver.find_element(By.XPATH, self.text_box_login_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_login_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_close(self):
        self.driver.find_element(By.XPATH, self.close_button_xpath).click()
