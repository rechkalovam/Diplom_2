#requests
CREATE_ORDER_BODY_WITHOUT_INGREDIENTS = {
            "ingredients": []
        }
CREATE_ORDER_BODY_WITH_NOT_VALID_INGREDIENTS = {
            "ingredients": ["12345fhsdffds", "feshf42342jadsdc"]
        }

#responses
CREATE_ORDER_ERROR_WITHOUT_INGREDIENTS_MESSAGE = {
    "success": False,
    "message": "Ingredient ids must be provided"
}