import pytest
import allure
from methods.order_methods import OrderMethods
from helpers import HelpersMethods
from data import EMPTY_TOKEN, EMPTY_BODY
from payloads.orders.create_order import (CREATE_ORDER_BODY_WITHOUT_INGREDIENTS, CREATE_ORDER_ERROR_WITHOUT_INGREDIENTS_MESSAGE,
                                          CREATE_ORDER_BODY_WITH_NOT_VALID_INGREDIENTS)

class TestCreateOrder:

    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_login_user_order_is_created_success(self, login_user):
        order_data = HelpersMethods.generate_order_data()
        status, message = OrderMethods().create_order(login_user, order_data)
        assert status == 200 and message["success"] == True, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Успешное создание заказа неавторизованным пользователем")
    def test_create_order_not_login_user_order_is_created_success(self):
        order_data = HelpersMethods.generate_order_data()
        status, message = OrderMethods().create_order(EMPTY_TOKEN, order_data)
        assert status == 200 and message["success"] == True, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка создания заказа с пустым телом ответа и пустым списком ingredients")
    @pytest.mark.parametrize('order_data', [EMPTY_BODY, CREATE_ORDER_BODY_WITHOUT_INGREDIENTS])
    def test_create_order_empty_order_is_not_created_error(self, login_user, order_data):
        status, message = OrderMethods().create_order(login_user, order_data)
        assert status == 400 and message == CREATE_ORDER_ERROR_WITHOUT_INGREDIENTS_MESSAGE, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка создания заказа с невалидными id ингредиентов")
    def test_create_order_not_valid_ingredients_order_is_not_created_error(self, login_user):
        order_data = CREATE_ORDER_BODY_WITH_NOT_VALID_INGREDIENTS
        status, message = OrderMethods().create_order(login_user, order_data)
        assert status == 500, f'Полученный код ответа: {status}, тело ответа: {message}'
