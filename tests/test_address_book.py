import unittest

from models.record import Record
from services.address_book import AddressBook


class TestAddressBook(unittest.TestCase):

    def setUp(self):
        self.book = AddressBook()

    def create_contact(
        self,
        name="John",
        phone="0501234567",
        email="john@gmail.com",
        birthday="15.09.1990",
    ):
        record = Record(name)
        record.add_phone(phone)
        record.add_email(email)
        record.add_birthday(birthday)

        self.book.add_record(record)

        return record

    def test_add_contact(self):
        record = self.create_contact()

        result = self.book.find("John")

        self.assertIsNotNone(result)
        self.assertEqual(result.name.value, "John")

    def test_duplicate_contact(self):
        self.create_contact()

        duplicate = Record("John")
        duplicate.add_phone("0671234567")

        result = self.book.add_record(duplicate)

        self.assertFalse(result)

    def test_find_contact_by_name(self):
        self.create_contact()

        result = self.book.search("John")

        self.assertIsNotNone(result)
        self.assertEqual(result.name.value, "John")

    def test_find_contact_by_phone(self):
        self.create_contact()

        result = self.book.search("0501234567")

        self.assertIsNotNone(result)

    def test_find_contact_by_email(self):
        self.create_contact()

        result = self.book.search("john@gmail.com")

        self.assertIsNotNone(result)

    def test_edit_phone(self):
        self.create_contact()

        result = self.book.edit_phone(
            "John",
            "0501234567",
            "0677654321",
        )

        self.assertTrue(result)

        contact = self.book.find("John")

        self.assertEqual(
            contact.phones[0].value,
            "0677654321",
        )

    def test_edit_email(self):
        self.create_contact()

        result = self.book.edit_email(
            "John",
            "john@gmail.com",
            "new@gmail.com",
        )

        self.assertTrue(result)

        contact = self.book.find("John")

        self.assertEqual(
            contact.email.value,
            "new@gmail.com",
        )

    def test_remove_phone(self):
        self.create_contact()

        result = self.book.remove_phone(
            "John",
            "0501234567",
        )

        self.assertTrue(result)

        contact = self.book.find("John")

        self.assertEqual(len(contact.phones), 0)

    def test_get_all_contacts(self):
        self.create_contact("John")
        self.create_contact(
            "Jane",
            "0671234567",
            "jane@gmail.com",
            "20.10.1992",
        )

        contacts = self.book.get_all()

        self.assertEqual(len(contacts), 2)


if __name__ == "__main__":
    unittest.main()