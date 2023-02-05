import time
import allure
import pytest

from Web.Pages.contact_page import Contact
from Utils.base import Base
from Web.Locators.locators_contact import Contact_locator


class Test_contact(Base, Contact_locator):

    @allure.description("contact button clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_button_clicked(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        assert title == "STORE"

    @allure.description("contact send message with correct email, name and message clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_valid_email_name_and_messgae(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Thanks for the message!!"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with incorrect email name and message clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_invalid_email_name_and_messgae(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.invalid_contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.invalid_contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.invalid_contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "invalid contact email and name"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with blank email name and message clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_empty_email_name_and_messgae(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.empty_contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.empty_contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.empty_contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "please fill out email, name and message"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with correct email, empty name and message clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_valid_email_empty_name_and_messgae(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.empty_contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.empty_contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "please fill out name and message"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with valid email and name and blank message clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_valid_email_and_name_and_empty_messgae(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.empty_contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "please fill out message"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with valid email and message empty name clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_will_send_message_with_valid_email_and_message_and_empty_name(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.empty_contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.contact_message)
        time.sleep(2)
        self.contact.click_contact_send_messgae_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "please fill out name"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("contact send message with valid email and message empty name clicked or not test")
    @pytest.mark.sanity
    def test_if_contact_us_close_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.contact = Contact(self.driver)
        time.sleep(2)
        self.contact.click_contact_button()
        time.sleep(2)
        self.contact.click_contact_email(self.contact_email)
        time.sleep(2)
        self.contact.click_contact_name(self.contact_name)
        time.sleep(2)
        self.contact.click_contact_message(self.contact_message)
        time.sleep(2)
        self.contact.click_contact_close_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()


