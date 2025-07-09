import requests
import allure
from requests.exceptions import JSONDecodeError
from urls import BASE_URL, USERS_URL


class UserMethods:

    @allure.step("Регистрация пользователя")
    def register_user(self, data):
        response = requests.post(f'{BASE_URL}{USERS_URL}/register', data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Авторизация пользователя")
    def login_user(self, data):
        response = requests.post(f'{BASE_URL}{USERS_URL}/login', data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Изменение данных пользователя")
    def change_user_data(self, token, data):
        response = requests.patch(f'{BASE_URL}{USERS_URL}/user', headers={'Authorization': f'{token}'}, data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        response = requests.delete(f'{BASE_URL}{USERS_URL}/user', headers={'Authorization': f'{token}'})
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text