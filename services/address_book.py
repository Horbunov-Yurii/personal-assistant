from models.record import Record
from datetime import date, datetime


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        if self.exists(str(record.name)):
            return False

        self.records.append(record)
        return True

    def find(self, name):
        for record in self.records:
            if str(record.name).lower() == name.lower():
                return record

        return None

    def exists(self, name):
        return self.find(name) is not None

    def find_by_email(self, email):
        for record in self.records:
            if record.email and record.email.value.lower() == email.lower():
                return record

        return None

    def find_by_phone(self, phone):
        for record in self.records:
            for item in record.phones:
                if str(item) == phone:
                    return record

        return None

    def search(self, query):
        for record in self.records:
            if str(record.name).lower() == query.lower():
                return record

            for phone in record.phones:
                if str(phone) == query:
                    return record

            if record.email and record.email.value.lower() == query.lower():
                return record

        return None

    def delete(self, name):
        record = self.find(name)

        if record is None:
            return False

        self.records.remove(record)
        return True

    def edit_phone(self, name, old_phone, new_phone):
        record = self.find(name)

        if record is None:
            return False

        return record.edit_phone(old_phone, new_phone)

    def remove_phone(self, name, phone):
        record = self.find(name)

        if record is None:
            return False

        return record.remove_phone(phone)

    def edit_email(self, name, old_email, new_email):
        record = self.find(name)

        if record is None:
            return False

        return record.edit_email(old_email, new_email)

    def get_upcoming_birthdays(self, days=7):
        today = date.today()
        upcoming = []

        for record in self.records:
            if record.birthday is None:
                continue

            birthday = datetime.strptime(
                record.birthday.value,
                "%d.%m.%Y",
            ).date()

            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_left = (birthday_this_year - today).days

            if days_left <= days:
                upcoming.append((record, birthday_this_year))

        return upcoming

    def get_all(self):
        return self.records


if __name__ == "__main__":
    book = AddressBook()

    john = Record("John")
    john.add_phone("380501111111")
    john.add_birthday("28.08.1990")

    anna = Record("Anna")
    anna.add_phone("380671234567")
    anna.add_birthday("15.09.1995")

    print("Adding John:", book.add_record(john))
    print("Adding Anna:", book.add_record(anna))

    duplicate_john = Record("JOHN")
    duplicate_john.add_phone("380502222222")

    print("Adding duplicate John:", book.add_record(duplicate_john))

    print("\nAll contacts:")

    for record in book.get_all():
        print(record)

    upcoming = book.get_upcoming_birthdays(7)

    print("\nUpcoming birthdays:")

    for record, birthday in upcoming:
        print(f"{record.name}: {birthday.strftime('%d.%m.%Y')}")
