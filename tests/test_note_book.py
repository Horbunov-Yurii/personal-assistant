import unittest

from models.note import Note
from services.note_book import NoteBook


class TestNoteBook(unittest.TestCase):

    def setUp(self):
        self.note_book = NoteBook()

    def create_note(
        self,
        title="Shopping",
        content="Buy milk",
        tags=None,
    ):
        if tags is None:
            tags = ["shopping", "home"]

        note = Note(title, content, tags)

        self.note_book.add_note(note)

        return note

    def test_add_note(self):
        self.create_note()

        note = self.note_book.find("Shopping")

        self.assertIsNotNone(note)
        self.assertEqual(note.title, "Shopping")

    def test_find_note(self):
        self.create_note()

        note = self.note_book.find("Shopping")

        self.assertIsNotNone(note)
        self.assertEqual(note.content, "Buy milk")

    def test_edit_note(self):
        self.create_note()

        result = self.note_book.edit(
            "Shopping",
            "Buy bread",
        )

        self.assertTrue(result)

        note = self.note_book.find("Shopping")

        self.assertEqual(
            note.content,
            "Buy bread",
        )

    def test_delete_note(self):
        self.create_note()

        result = self.note_book.delete("Shopping")

        self.assertTrue(result)

        note = self.note_book.find("Shopping")

        self.assertIsNone(note)

    def test_find_note_by_tag(self):
        self.create_note()

        notes = self.note_book.find_by_tag("shopping")

        self.assertEqual(len(notes), 1)
        self.assertEqual(
            notes[0].title,
            "Shopping",
        )

    def test_get_all_notes(self):
        self.create_note("Shopping")

        self.create_note(
            "Work",
            "Finish project",
            ["work"],
        )

        notes = self.note_book.get_all()

        self.assertEqual(len(notes), 2)


if __name__ == "__main__":
    unittest.main()