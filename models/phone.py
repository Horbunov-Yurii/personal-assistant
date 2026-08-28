import re


class Phone:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid phone number")

        self.value = value

    @staticmethod
    def is_valid(value):
        pattern = r"^\+?[0-9]{10,15}$"
        return bool(re.fullmatch(pattern, value))

    def __str__(self):
        return self.value


if __name__ == "__main__":
    phone = Phone("380501234567")

    print(phone)
    print(Phone.is_valid("380501234567"))
    print(Phone.is_valid("12345"))
