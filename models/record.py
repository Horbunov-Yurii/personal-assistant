from models.email import Email
from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.email = Email(email)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)    

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[index] = Phone(new_phone)
                return True

        return False

    def remove_phone(self, phone):
        for item in self.phones:
            if str(item) == phone:
                self.phones.remove(item)
                return True

        return False
    
    def edit_email(self, old_email, new_email):
        if self.email and self.email.value == old_email:
            self.email = Email(new_email)
            return True

        return False
    
    def remove_email(self):
        if self.email:
            self.email = None
            return True

        return False

    def __str__(self):
        phones = ", ".join(str(phone) for phone in self.phones)
        email = str(self.email) if self.email else "Not specified"
        birthday = str(self.birthday) if self.birthday else "Not specified"

        return (
            f"Name: {self.name}\n"
            f"Phones: {phones}\n"
            f"Email: {email}\n"
            f"Birthday: {birthday}"
        )
    

if __name__ == "__main__":
    record = Record("John")
    record.add_phone("380501234567")
    record.add_email("john@example.com")
    record.add_birthday("15.09.1990")

    print("Before:")
    print(record)

    result = record.remove_email()

    print("\nResult:", result)

    print("\nAfter:")
    print(record)
