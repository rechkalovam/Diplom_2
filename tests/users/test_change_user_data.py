import pytest
import allure
from methods.user_methods import UserMethods
from payloads.users.change_user_data import (CHANGE_USER_EMAIL, CHANGE_USER_NAME, CHANGE_USER_PASSWORD,
                                             CHANGE_USER_DATA_ERROR_NOT_LOGIN_MESSAGE)
from data import EMPTY_TOKEN


class TestChangeUserData:

    @allure.title("Успешное изменение email, пароля и имени авторизованного пользователя ")
    @pytest.mark.parametrize('data', [CHANGE_USER_EMAIL, CHANGE_USER_NAME, CHANGE_USER_PASSWORD])
    def test_change_user_data_login_user_data_is_changed_success(self, login_user, data):
        status, message = UserMethods().change_user_data(login_user, data)
        assert status == 200 and message["success"] == True, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка изменения email, пароля и имени пользователя неавторзованного пользователя")
    @pytest.mark.parametrize('data', [CHANGE_USER_EMAIL, CHANGE_USER_NAME, CHANGE_USER_PASSWORD])
    def test_change_user_data_not_login_user_data_is_not_changed_error(self, data):
        status, message = UserMethods().change_user_data(EMPTY_TOKEN, data)
        assert status == 401 and message == CHANGE_USER_DATA_ERROR_NOT_LOGIN_MESSAGE, f'Полученный код ответа: {status}, тело ответа: {message}'
