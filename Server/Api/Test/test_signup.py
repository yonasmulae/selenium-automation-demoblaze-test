import requests
import allure
from Server.Api.Constants.signup_constants_ import Signup_api_locators


class Test_signup_api:
    @allure.description('Login correctly when data is valid')
    def test_signup_correctly(self):
        url = "https://api.demoblaze.com/signup"
        data = Signup_api_locators.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Signup_api_locators.success_key] == True

    @allure.description('Login incorrectly when email is invalid')
    def test_sign_up_when_email_is_invalid(self):
        url = "https://api.demoblaze.com/signup"
        data = Signup_api_locators.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Signup_api_locators.success_key] == True

    @allure.description('Login incorrectly when password is invalid')
    def test_test_sign_up_when_password_is_invalid(self):
        url = "https://api.demoblaze.com/signup"
        data = Signup_api_locators.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Signup_api_locators.success_key] == True

    @allure.description('Login incorrectly when email and password is invalid')
    def test_login_when_email_and_password_is_invalid(self):
        url = "https://api.demoblaze.com/login"
        data = Signup_api_locators.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Login_api_locators.success_key] == True


