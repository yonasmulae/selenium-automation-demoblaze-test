from selenium.webdriver.common.by import By
from Web.Locators.locators_contact import Contact_locator


class Contact(Contact_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_contact_button(self):
        self.driver.find_element(By.XPATH, self.contact_button_xpath).click()

    def click_contact_email(self, contact_email):
        self.driver.find_element(By.XPATH, self.contact_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.contact_email_xpath).send_keys(contact_email)

    def click_contact_name(self, contact_name):
        self.driver.find_element(By.XPATH, self.contact_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.contact_name_xpath).send_keys(contact_name)

    def click_contact_message(self, contact_messgae):
        self.driver.find_element(By.XPATH, self.contact_message_xpath).clear()
        self.driver.find_element(By.XPATH, self.contact_message_xpath).send_keys(contact_messgae)

    def click_contact_send_messgae_button(self):
        self.driver.find_element(By.XPATH, self.send_message_button_xpath).click()

    def click_contact_close_button(self):
        self.driver.find_element(By.XPATH, self.close_button_xpath).click()
