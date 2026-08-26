from email_validator import EmailNotValidError, validate_email


class Email:
    def __init__(self, value):
        self.value = self.validate(value)

    @staticmethod
    def validate(value):
        try:
            result = validate_email(value, check_deliverability=False)
            return result.normalized
        except EmailNotValidError:
            raise ValueError("Invalid email address")

    def __str__(self):
        return self.value
    


if __name__ == "__main__":
    valid_email = Email("john@example.com")

    print("Valid:")
    print(valid_email)

    try:
        invalid_email = Email("hello")
        print(invalid_email)
    except ValueError as error:
        print("Error:", error)    