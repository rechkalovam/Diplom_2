#requests
REGISTER_USER_WITHOUT_EMAIL = {
    "password": "768852",
    "name": "jklzcoq"
}
REGISTER_USER_WITHOUT_PASSWORD = {
    "email": "y4c03x3g@example_test.ru",
    "name": "jklzcoq"
}
REGISTER_USER_WITHOUT_NAME = {
    "email": "y4c03x3g@example_test.ru",
    "password": "768852"
}

#responses
USER_ALREADY_EXIST_ERROR = {
    "success": False,
    "message": "User already exists"
}
MISSING_REQUIRED_FIELDS_ERROR = {
    "success": False,
    "message": "Email, password and name are required fields"
}