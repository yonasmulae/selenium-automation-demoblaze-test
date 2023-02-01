import time
import allure
import pytest
from Web.Pages.home_page import Home
from Web.Pages.cart_page import Cart
from Utils.base import Base
from Web.Locators.locator_cart import Cart_locator


class Test_Cart(Base, Cart_locator):

    @allure.description("Cart button clicked or not test")
    @pytest.mark.sanity
    def test_if_cart_button_clicked(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_phone_button()
        time.sleep(2)
        self.add_to_cart.click_phone_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("Cart delete button works or not test")
    @pytest.mark.sanity
    def test_cart_page_delete_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_phone_button()
        time.sleep(2)
        self.add_to_cart.click_phone_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        self.add.click_delete_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("Cart place order button clicked or not test")
    @pytest.mark.sanity
    def test_cart_page_place_order_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_phone_button()
        time.sleep(2)
        self.add_to_cart.click_phone_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        self.add.click_place_order_button()
        time.sleep(2)
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("Cart purchase button clicked or not test")
    @pytest.mark.sanity
    def test_cart_page_purchase_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_phone_button()
        time.sleep(2)
        self.add_to_cart.click_phone_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        self.add.click_place_order_button()
        time.sleep(2)
        self.add.click_place_order_name_input(self.place_order_name)
        time.sleep(2)
        self.add.click_place_order_country_input(self.place_order_coutry)
        time.sleep(2)
        self.add.click_place_order_city_input(self.place_order_city)
        time.sleep(2)
        self.add.click_place_order_credit_card_input(self.place_order_credit_card)
        time.sleep(2)
        self.add.click_place_order_month_input(self.place_order_month)
        time.sleep(2)
        self.add.click_place_order_year_input(self.place_order_year)
        time.sleep(2)
        self.add.click_Purchase_button()
        time.sleep(2)
        self.add.click_perchase_order_message_ok()
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("Cart button clicked or not test")
    @pytest.mark.sanity
    def test_cart_page_laptop_product_added_E2E_test(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_laptop_button()
        time.sleep(2)
        self.add_to_cart.click_laptop_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        self.add.click_place_order_button()
        time.sleep(2)
        self.add.click_place_order_name_input(self.place_order_name)
        time.sleep(2)
        self.add.click_place_order_country_input(self.place_order_coutry)
        time.sleep(2)
        self.add.click_place_order_city_input(self.place_order_city)
        time.sleep(2)
        self.add.click_place_order_credit_card_input(self.place_order_credit_card)
        time.sleep(2)
        self.add.click_place_order_month_input(self.place_order_month)
        time.sleep(2)
        self.add.click_place_order_year_input(self.place_order_year)
        time.sleep(2)
        self.add.click_Purchase_button()
        time.sleep(2)
        self.add.click_perchase_order_message_ok()
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False

    @allure.description("Cart button clicked or not test")
    @pytest.mark.sanity
    def test_cart_page_monitor_product_added_E2E_test(self):
        self.driver = super().init()
        time.sleep(2)
        self.add_to_cart = Home(self.driver)
        time.sleep(2)
        self.add_to_cart.click_catagories_monitors_button()
        time.sleep(2)
        self.add_to_cart.click_monitors_product()
        time.sleep(2)
        self.add_to_cart.click_add_to_cart_button()
        time.sleep(2)
        popup = self.driver.switch_to.alert.text
        assert popup == "Product added"
        self.driver.switch_to.alert.accept()
        self.add = Cart(self.driver)
        time.sleep(2)
        self.add.click_cart_button()
        time.sleep(2)
        self.add.click_place_order_button()
        time.sleep(2)
        self.add.click_place_order_name_input(self.place_order_name)
        time.sleep(2)
        self.add.click_place_order_country_input(self.place_order_coutry)
        time.sleep(2)
        self.add.click_place_order_city_input(self.place_order_city)
        time.sleep(2)
        self.add.click_place_order_credit_card_input(self.place_order_credit_card)
        time.sleep(2)
        self.add.click_place_order_month_input(self.place_order_month)
        time.sleep(2)
        self.add.click_place_order_year_input(self.place_order_year)
        time.sleep(2)
        self.add.click_Purchase_button()
        time.sleep(2)
        self.add.click_perchase_order_message_ok()
        title = self.driver.title
        super().tear_down()
        if title == "STORE":
            assert True
        else:
            assert False
