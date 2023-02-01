from selenium.webdriver.common.by import By
from Web.Locators.locators_signup import Sign_up_locator


class Sign_up(Sign_up_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_sign_up_link(self):
        self.driver.find_element(By.XPATH, self.sign_up_button_link_xpath).click()

    def set_user_name(self, username):
        self.driver.find_element(By.XPATH, self.sign_up_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.sign_up_username_xpath).send_keys(username)

    def set_user_password(self, password):
        self.driver.find_element(By.XPATH, self.sign_up_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.sign_up_password_xpath).send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(By.XPATH, self.sign_up_button).click()

    def click_close(self):
        self.driver.find_element(By.XPATH, self.close_button).click()
