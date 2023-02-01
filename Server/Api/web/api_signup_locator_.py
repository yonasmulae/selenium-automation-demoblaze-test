
class Signup_api_locators:
    url = "https://api.demoblaze.com/signup"
    success_key = "success"
    message_key = "message"
    data_valid = {"email": "qataster67@gmail.com", "password": "yonasamare7"}
    data_invalid_password = {"email": "qataster67@gmail.com", "password": "@#$%&"}
    data_invalid_email = {"email": "%555", "password": "yonasamare7"}
    data_invalid_password_and_email = {"email": "%555", "password": "20202020"}
