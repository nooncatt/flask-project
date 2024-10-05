# models.py
import re

class User:
    # todo: user class
    def __init__(self, id, first_name, last_name, phone, email, score=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.score = score

    @staticmethod
    def is_valid_email(email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return True
        else:
            return False

    @staticmethod
    def is_valid_phone(phone):
        if re.match(r"^\+?[1-9][0-9]{7,14}$", phone):
            return True
        else:
            return False

