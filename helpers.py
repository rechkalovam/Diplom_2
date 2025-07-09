import random
import string


class HelpersMethods:

    @staticmethod
    def generate_user_data():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@example.ru'
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        password = ''.join(random.choice(string.digits) for _ in range(random.randint(4, 8)))
        return {
            "email": email,
            "password": password,
            "name": username
        }

    @staticmethod
    def generate_new_user_email():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@new-example.ru'
        return email

    @staticmethod
    def generate_order_data():
        buns = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6c"]
        sauces = ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa73", "61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa75"]
        fillings = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa6e",
                    "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa78", "61c0c5a71d1f82001bdaaa79",
                    "61c0c5a71d1f82001bdaaa7a"]
        order = {
            "ingredients": [
                random.choice(buns),
                random.choice(sauces),
                random.choice(fillings)
            ]
        }
        return order