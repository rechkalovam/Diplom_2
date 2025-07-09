import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
from helpers import HelpersMethods


@pytest.fixture()
def create_user():
    user_data = HelpersMethods.generate_user_data()
    response = UserMethods().register_user(user_data)
    yield user_data, response[1]["accessToken"]
    UserMethods().delete_user(response[1]["accessToken"])

@pytest.fixture()
def login_user(create_user):
    user_data, access_token = create_user
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    response = UserMethods().login_user(login_data)
    return response[1]["accessToken"]

@pytest.fixture()
def delete_user(create_user):
    user_data, access_token = create_user
    UserMethods().delete_user(access_token)
    return {
            "email": user_data["email"],
            "password": user_data["password"]
    }

@pytest.fixture()
def create_order(login_user):
    order_data = HelpersMethods.generate_order_data()
    OrderMethods().create_order(login_user, order_data)
    return login_user