import time
import allure
import pytest

from Web.Pages.home_page import Home
from Main.base import Base
from Web.Locators.locators_home import Home_locator


class Test_home(Base, Home_locator):

    @allure.description("Homepage will refresh or not test")
    @pytest.mark.sanity
    def test_if_homepage_refresh_or_not(self):
        self.driver = super().init()
        time.sleep(2)
        self.refresh = Home(self.driver)
        time.sleep(2)
        self.refresh.click_homepage_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage slider view previous button clicked or not test")
    @pytest.mark.sanity
    def test_if_homepage_prevoius_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.previous = Home(self.driver)
        time.sleep(2)
        self.previous.click_homepage_previous_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage slider view next button clicked or not test")
    @pytest.mark.sanity
    def test_if_homepage_next_button_works(self):
        self.driver = super().init()
        time.sleep(2)
        self.next = Home(self.driver)
        time.sleep(2)
        self.next.click_homepage_next_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories phone button click or not test")
    @pytest.mark.sanity
    def test_if_catagories_phone_button_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.phone = Home(self.driver)
        time.sleep(2)
        self.phone.click_catagories_phone_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories phone product clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_phone_nexus_6_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.product = Home(self.driver)
        time.sleep(2)
        self.product.click_phone_product()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories phone product added to cart or not test")
    @pytest.mark.sanity
    def test_if_catagories_phone_nexus_6_added_to_cart(self):
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

    @allure.description("Homepage categories laptop button clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_laptop_button_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.phone = Home(self.driver)
        time.sleep(2)
        self.phone.click_catagories_laptop_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories laptop product is clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_laptop_product_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.product = Home(self.driver)
        time.sleep(2)
        self.product.click_laptop_product()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories laptop product is clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_laptop_product_is_added_to_cart(self):
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

    @allure.description("Homepage categories monitors button clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_monitors_button_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.phone = Home(self.driver)
        time.sleep(2)
        self.phone.click_catagories_monitors_button()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories monitors product clicked or not test")
    @pytest.mark.sanity
    def test_if_catagories_monitors_product_is_clickable(self):
        self.driver = super().init()
        time.sleep(2)
        self.product = Home(self.driver)
        time.sleep(2)
        self.product.click_monitors_product()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    @allure.description("Homepage categories monitors product added to cart or not test")
    @pytest.mark.sanity
    def test_if_catagories_monitors_product_is_added_to_cart(self):
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

    @allure.description("Homepage footer page is presented or not test")
    @pytest.mark.sanity
    def test_if_the_footer_page_is_presented(self):
        self.driver = super().init()
        time.sleep(2)
        self.footer_page = Home(self.driver)
        time.sleep(2)
        self.footer_page.check_footer_page()
        time.sleep(2)
        title = self.driver.title
        assert title == "STORE"
        super().tear_down()

    # def test_yo(self):
    #     self.driver = super().init()
    #     time.sleep(2)
    #     self.footer_page = Home(self.driver)
    #     time.sleep(2)
    #     p = self.driver.find_element(By.XPATH, self.p)
    #     d = p.find_elements(By.TAG_NAME, self.d)
    #
    #     l = 0
    #     for x in d(range(6)):
    #         l += 1
    #         time.sleep(2)
    #         x.click()
    #         time.sleep(2)
    #
    #         break
    #     super().tear_down()


