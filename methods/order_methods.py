import requests
import allure
from requests.exceptions import JSONDecodeError
from urls import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step("Создание заказа")
    def create_order(self, token, data):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', headers={'Authorization': f'{token}'}, data=data)
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Получение заказа пользователя")
    def get_user_orders(self, token):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers={'Authorization': f'{token}'})
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

