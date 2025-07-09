import allure
from methods.user_methods import UserMethods
from payloads.users.login_user import INCORRECT_CREDENTIALS_ERROR


class TestLoginUser:

    @allure.title("Успешная авторизация зарегистрированного пользователя")
    def test_login_user_is_registered_success(self, create_user):
        user_data, access_token = create_user
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        status, message = UserMethods().login_user(login_data)
        assert status == 200 and message["success"] == True, f'Полученный код ответа: {status}, тело ответа: {message}'

    @allure.title("Попытка регистрации с невалидным логином и паролем")
    def test_login_user_not_registered_error(self, delete_user):
        status, message = UserMethods().login_user(delete_user)
        assert status == 401 and message == INCORRECT_CREDENTIALS_ERROR, f'Полученный код ответа: {status}, тело ответа: {message}'