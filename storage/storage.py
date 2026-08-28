import json
import os
import pickle

from models.record import Record
from models.note import Note
from services.address_book import AddressBook
from services.note_book import NoteBook


def save_data(data, filename):
    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_data(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


def export_to_json(book, note_book, filename):
    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)

    contacts = []

    for record in book.get_all():
        birthday = record.birthday

        if birthday is not None:
            if hasattr(birthday, "strftime"):
                birthday = birthday.strftime("%d.%m.%Y")
            else:
                birthday = str(birthday)

        contacts.append(
            {
                "name": str(record.name),
                "phones": [str(phone) for phone in record.phones],
                "email": (str(record.email) if record.email else None),
                "birthday": birthday,
            }
        )

    notes = []

    for note in note_book.get_all():
        notes.append(
            {
                "title": str(note.title),
                "content": str(note.content),
                "tags": [str(tag) for tag in note.tags],
            }
        )

    data = {
        "contacts": contacts,
        "notes": notes,
    }

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )


def import_from_json(filename):
    with open(
        filename,
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object.")

    if "contacts" not in data:
        raise KeyError("Missing 'contacts' field.")

    if "notes" not in data:
        raise KeyError("Missing 'notes' field.")

    if not isinstance(data["contacts"], list):
        raise TypeError("'contacts' must be a list.")

    if not isinstance(data["notes"], list):
        raise TypeError("'notes' must be a list.")

    book = AddressBook()
    note_book = NoteBook()

    for contact in data["contacts"]:
        if not isinstance(contact, dict):
            raise ValueError("Invalid contact format.")

        if "name" not in contact:
            raise KeyError("Contact is missing 'name'.")

        record = Record(contact["name"])

        for phone in contact.get("phones", []):
            record.add_phone(phone)

        email = contact.get("email")

        if email:
            record.add_email(email)

        birthday = contact.get("birthday")

        if birthday:
            record.add_birthday(birthday)

        book.add_record(record)

    for note_data in data["notes"]:
        if not isinstance(note_data, dict):
            raise ValueError("Invalid note format.")

        if "title" not in note_data:
            raise KeyError("Note is missing 'title'.")

        title = note_data["title"]
        content = note_data.get("content", "")
        tags = note_data.get("tags", [])

        if not isinstance(tags, list):
            raise TypeError("Note 'tags' must be a list.")

        note = Note(
            title,
            content,
            tags,
        )

        note_book.add_note(note)

    return book, note_book
