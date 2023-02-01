import time
import allure
import pytest

from Web.Pages.about_us_page import About_us
from Utils.base import Base
from Web.Locators.locators_about_us import About_us_locator


class Test_about_us(Base, About_us_locator):

    @allure.description("About us button clicked or not test")
    @pytest.mark.sanity
    def test_About_us_button_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play clicked or not test")
    @pytest.mark.sanity
    def test_About_us_play_video_is_clicked(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play paused button clicked or not test")
    @pytest.mark.sanity
    def test_if_About_us_play_video_is_paused(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        self.about_us.click_About_us_video_pause_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play volume button clicked or not test")
    @pytest.mark.sanity
    def test_if_About_us_play_video_volume_will_mute(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        self.about_us.click_About_us_video_volume_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play picture in picture button clicked or not test")
    @pytest.mark.sanity
    def test_if_About_us_play_video_picture_in_picture_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        self.about_us.click_About_us_video_picture_in_picture_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play full-screen button clicked or not test")
    @pytest.mark.sanity
    def test_if_About_us_play_video_fullscreen_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        self.about_us.click_About_us_video_fullscreen_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("About us video play close button clicked or not test")
    @pytest.mark.sanity
    def test_if_About_us_play_video_close_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.about_us = About_us(self.driver)
        time.sleep(2)
        self.about_us.click_About_us_button()
        time.sleep(2)
        self.about_us.click_About_us_play_video_button()
        time.sleep(2)
        self.about_us.click_About_us_video_close_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

