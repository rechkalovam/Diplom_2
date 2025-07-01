import pytest
import allure
from methods.user_methods import UserMethods
from helpers import HelpersMethods
from payloads.users.register_user import (USER_ALREADY_EXIST_ERROR, REGISTER_USER_WITHOUT_EMAIL, REGISTER_USER_WITHOUT_NAME,
                                          REGISTER_USER_WITHOUT_PASSWORD, MISSING_REQUIRED_FIELDS_ERROR)


class TestRegisterUser:

    @allure.title("Успешная регистрация пользователя")
    def test_register_user_user_is_registered_success(self):
        user_data = HelpersMethods.generate_user_data()
        status, message = UserMethods().register_user(user_data)
        assert status == 200 and message["success"] == True, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка регистрации уже зарегистрированного пользователя")
    def test_register_user_user_already_registered_error(self, create_user):
        user_data, access_token = create_user
        status, message = UserMethods().register_user(user_data)
        assert status == 403 and message == USER_ALREADY_EXIST_ERROR, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка регистрации пользователя без заполнения обязательных полей")
    @pytest.mark.parametrize('user_data', [REGISTER_USER_WITHOUT_EMAIL, REGISTER_USER_WITHOUT_NAME, REGISTER_USER_WITHOUT_PASSWORD])
    def test_register_user_without_required_fields_not_registered_error(self, user_data):
        status, message = UserMethods().register_user(user_data)
        assert status == 403 and message == MISSING_REQUIRED_FIELDS_ERROR, f'Полученный код ответа: {status}, тело ответа: {message}'