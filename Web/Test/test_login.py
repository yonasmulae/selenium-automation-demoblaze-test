import time
import allure
import pytest
from Web.Pages.login_page import Login
from Utils.base import Base
from Web.Locators.locators_login import login_locator


class Test_login(Base, login_locator):
    @allure.description("Login link button clickable test")
    @pytest.mark.sanity
    def test_login_link_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.click = Login(self.driver)
        time.sleep(2)
        self.click.click_login_link()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Login user test with all valid fields")
    @pytest.mark.sanity
    def test_check_user_will_login_with_valid_username_and_password(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        time.sleep(2)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.username)
        time.sleep(2)
        self.login_page.set_user_password(self.password)
        time.sleep(2)
        self.login_page.click_login()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Login user with correct username and incorrect password")
    @pytest.mark.sanity
    def test_check_user_will_login_with_valid_username_and_empty_password(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.username)
        time.sleep(2)
        self.login_page.set_user_password(self.empty_password)
        time.sleep(2)
        self.login_page.click_login()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Login user with incorrect username and correct password")
    @pytest.mark.sanity
    def test_check_user_will_login_with_empty_username_valid_password(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.empty_username)
        time.sleep(2)
        self.login_page.set_user_password(self.password)
        time.sleep(2)
        self.login_page.click_login()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Login user with non exist username and password test")
    @pytest.mark.sanity
    def test_check_user_will_login_with_empty_username_and_password(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.empty_username)
        time.sleep(2)
        self.login_page.set_user_password(self.empty_password)
        time.sleep(2)
        self.login_page.click_login()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Login link button clickable test")
    @pytest.mark.sanity
    def test_check_user_will_login_with_invalid_username_and_password(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.invalid_username)
        time.sleep(2)
        self.login_page.set_user_password(self.invalid_password)
        time.sleep(2)
        self.login_page.click_login()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "User does not exist."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Login box close button test")
    @pytest.mark.sanity
    def test_check_login_box_close_button_works(self):
        self.driver = super().init()
        self.login_page = Login(self.driver)
        self.login_page.click_login_link()
        time.sleep(2)
        self.login_page.set_user_name(self.username)
        time.sleep(2)
        self.login_page.set_user_password(self.password)
        time.sleep(2)
        self.login_page.click_close()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()
