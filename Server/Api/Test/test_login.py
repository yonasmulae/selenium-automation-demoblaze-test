import requests
import allure
from Server.Api.Constants.login_constants import Login_api_locators


class Test_login_api:
    @allure.description('Login correctly when data is valid')
    def test_login_correctly(self):
        url = "https://api.demoblaze.com/login"
        data = Login_api_locators.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Api_locators.success_key] == False

    @allure.description('Login incorrectly when email is invalid')
    def test_login_when_email_is_invalid(self):
        url = "https://api.demoblaze.com/login"
        data = Login_api_locators.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 20
        # assert res_data[Api_locators.success_key] == True

    @allure.description('Login incorrectly when password is invalid')
    def test_test_login_when_password_is_invalid(self):
        url = "https://api.demoblaze.com/login"
        data = Login_api_locators.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        assert res_data[Login_api_locators.success_key] == True

    @allure.description('Login incorrectly when email and password is invalid')
    def test_login_when_email_and_password_is_invalid(self):
        url = "https://api.demoblaze.com/login"
        data = Login_api_locators.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()

        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20
        assert res_data[Login_api_locators.success_key] == True

