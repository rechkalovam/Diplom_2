from helpers import HelpersMethods
#requests
CHANGE_USER_EMAIL = {
    "email": f'{HelpersMethods.generate_new_user_email()}',
}
CHANGE_USER_NAME = {
    "name": "Новое имя"
}
CHANGE_USER_PASSWORD = {
    "password": "qwerty12345"
}

#responses
CHANGE_USER_DATA_ERROR_NOT_LOGIN_MESSAGE = {
    "success": False,
    "message": "You should be authorised"
}