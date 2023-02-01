from selenium.webdriver.common.by import By
from Web.Locators.locator_cart import Cart_locator
from Web.Locators.locators_home import Home_locator


class Cart(Cart_locator, Home_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_cart_button(self):
        self.driver.find_element(By.XPATH, self.cart_button_xpath).click()

    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.delete_button_xpath).click()

    def click_place_order_button(self):
        self.driver.find_element(By.XPATH, self.place_order_button_xpath).click()

    def click_place_order_name_input(self, name):
        self.driver.find_element(By.XPATH, self.place_order_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_name_xpath).send_keys(name)

    def click_place_order_country_input(self, country):
        self.driver.find_element(By.XPATH, self.place_order_country_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_country_xpath).send_keys(country)

    def click_place_order_city_input(self, city):
        self.driver.find_element(By.XPATH, self.place_order_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_city_xpath).send_keys(city)

    def click_place_order_credit_card_input(self, credit_card):
        self.driver.find_element(By.XPATH, self.place_order_credit_card_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_credit_card_xpath).send_keys(credit_card)

    def click_place_order_month_input(self, month):
        self.driver.find_element(By.XPATH, self.place_order_month_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_month_xpath).send_keys(month)

    def click_place_order_year_input(self, year):
        self.driver.find_element(By.XPATH, self.place_order_year_xpath).clear()
        self.driver.find_element(By.XPATH, self.place_order_year_xpath).send_keys(year)

    def click_Purchase_button(self):
        self.driver.find_element(By.XPATH, self.perchase_button).click()

    def click_perchase_order_message_ok(self):
        self.driver.find_element(By.XPATH, self.perchase_message_ok).click()
