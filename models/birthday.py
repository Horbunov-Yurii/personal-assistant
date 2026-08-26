from datetime import datetime


class Birthday:
    def __init__(self, value):
        self.value = self.validate(value)

    @staticmethod
    def validate(value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return value
        except ValueError:
            raise ValueError("Invalid birthday. Use DD.MM.YYYY")

    def __str__(self):
        return self.value