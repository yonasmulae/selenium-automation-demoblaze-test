import time

from selenium.webdriver.common.by import By
from Web.Locators.locators_home import Home_locator


class Home(Home_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_homepage_button(self):
        self.driver.find_element(By.XPATH, self.homepage_button).click()

    def click_homepage_previous_button(self):
        self.driver.find_element(By.XPATH, self.previous_button_xpath).click()

    def click_homepage_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()

    def click_catagories_phone_button(self):
        self.driver.find_element(By.XPATH, self.catagories_phone_xpath).click()

    def click_catagories_laptop_button(self):
        self.driver.find_element(By.XPATH, self.catagories_laptops_xpath).click()

    def click_catagories_monitors_button(self):
        self.driver.find_element(By.XPATH, self.catagories_monitors_xpath).click()

    def click_phone_product(self):
        self.driver.find_element(By.XPATH, self.phone_nexus_6_xpath).click()

    def click_laptop_product(self):
        self.driver.find_element(By.XPATH, self.laptop_sony_vaio_i7).click()

    def click_monitors_product(self):
        self.driver.find_element(By.XPATH, self.monitor_apple_monitor_24).click()

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()

    def check_footer_page(self):
        self.driver.execute_script(self.scroll_down_1)
        time.sleep(2)
        self.driver.execute_script(self.scroll_down_2)

    def check_footer_page_about_us(self):
        self.driver.execute_script(self.scroll_down_1)
        time.sleep(2)
        self.driver.execute_script(self.scroll_down_2)
        self.driver.find_element(By.XPATH, self.about_us_text).get_attribute("innerHTML")

    def check_footer_page_get_in_touch(self):
        self.driver.execute_script(self.scroll_down_1)
        time.sleep(2)
        self.driver.execute_script(self.scroll_down_2)
        self.driver.find_element(By.XPATH, self.get_in_touch)

    def check_footer_page_product_store(self):
        self.driver.find_element(self.scroll_down_1)
        time.sleep(2)
        self.driver.execute_script(self.scroll_down_2)
        self.driver.execute_script(self.product_store_logo)




