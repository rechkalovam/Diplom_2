import allure
from methods.order_methods import OrderMethods
from data import EMPTY_TOKEN
from payloads.orders.get_user_orders import GET_USER_ORDERS_ERROR_NOT_LOGIN_MESSAGE


class TestGetUserOrders:

    @allure.title("Успешное получение заказа авторизованного пользователя")
    def test_get_user_orders_return_user_order_success(self, create_order):
        status, message = OrderMethods().get_user_orders(create_order)
        assert status == 200 and message["success"] == True and message["orders"] is not None, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка получить список заказов неавторизованного пользователя")
    def test_get_user_orders_not_login_user_orders_not_return_error(self):
        status, message = OrderMethods().get_user_orders(EMPTY_TOKEN)
        assert status == 401 and message == GET_USER_ORDERS_ERROR_NOT_LOGIN_MESSAGE, f'Полученный код ответа: {status}, тело ответа: {message}'
