import time
import allure
import pytest
from Web.Pages.signup_page import Sign_up
from Main.base import Base
from Web.Locators.locators_signup import Sign_up_locator


class Test_Sign_up(Base, Sign_up_locator):
    @allure.description("Sign_up link is clickable test")
    @pytest.mark.sanity
    def test_sign_up_link_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.click = Sign_up(self.driver)
        time.sleep(2)
        self.click.click_sign_up_link()
        time.sleep(2)

    @allure.description("Sign_up user with all valid fields")
    @pytest.mark.sanity
    def test_check_user_will_sign_up_with_valid_username_and_password(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.set_user_name(self.username)
        time.sleep(2)
        self.sign_up.set_user_password(self.password)
        time.sleep(2)
        self.sign_up.click_sign_up()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "This user already exist."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Sign_up user with correct user name and incorrect password")
    @pytest.mark.sanity
    def test_check_user_will_sign_up_with_valid_username_and_empty_password(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.set_user_name(self.username)
        time.sleep(2)
        self.sign_up.set_user_password(self.empty_password)
        time.sleep(2)
        self.sign_up.click_sign_up()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Sign_up user with all correct password and incorrect username")
    @pytest.mark.sanity
    def test_check_user_will_sign_up_with_empty_username_and_valid_password(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.set_user_name(self.empty_username)
        time.sleep(2)
        self.sign_up.set_user_password(self.password)
        time.sleep(2)
        self.sign_up.click_sign_up()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Sign_up user with blank username and password")
    @pytest.mark.sanity
    def test_check_user_will_sign_up_with_empty_username_and_password(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.set_user_name(self.empty_username)
        time.sleep(2)
        self.sign_up.set_user_password(self.empty_password)
        time.sleep(2)
        self.sign_up.click_sign_up()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Please fill out Username and Password."
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Sign_up user with not exist username and password")
    @pytest.mark.sanity
    def test_check_user_will_sign_up_with_invalid_username_and_password(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.set_user_name(self.invalid_username)
        time.sleep(2)
        self.sign_up.set_user_password(self.invalid_password)
        time.sleep(2)
        self.sign_up.click_sign_up()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "invalid username and password"
        self.driver.switch_to.alert.accept()
        super().tear_down()

    @allure.description("Sign_up user box close button test")
    @pytest.mark.sanity
    def test_check_sign_up_box_close_button_works(self):
        self.driver = super().init()
        self.sign_up = Sign_up(self.driver)
        self.sign_up.click_sign_up_link()
        time.sleep(2)
        self.sign_up.click_close()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()
