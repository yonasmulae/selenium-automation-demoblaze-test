from selenium.webdriver.common.by import By
from Web.Locators.locators_about_us import About_us_locator


class About_us(About_us_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_About_us_button(self):
        self.driver.find_element(By.XPATH, self.about_us_button_xpath).click()

    def click_About_us_play_video_button(self):
        self.driver.find_element(By.XPATH, self.play_video_xpath).click()

    def click_About_us_video_pause_button(self):
        self.driver.find_element(By.XPATH, self.pause_or_play_button).click()

    def click_About_us_video_volume_button(self):
        self.driver.find_element(By.XPATH, self.video_volume).click()

    def click_About_us_video_picture_in_picture_button(self):
        self.driver.find_element(By.XPATH, self.picture_in_picture_button).click()

    def click_About_us_video_fullscreen_button(self):
        self.driver.find_element(By.XPATH, self.full_screen_button).click()

    def click_About_us_video_close_button(self):
        self.driver.find_element(By.XPATH, self.close_button).click()