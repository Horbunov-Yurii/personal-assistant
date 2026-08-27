from models.note import Note


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def find(self, title):
        for note in self.notes:
            if note.title.lower() == title.lower():
                return note

        return None
    
    def edit(self, title, new_content):
        note = self.find(title)

        if note is None:
            return False

        note.content = new_content
        return True
    
    def delete(self, title):
        note = self.find(title)

        if note is None:
            return False

        self.notes.remove(note)
        return True
    

    def find_by_tag(self, tag):
        result = []

        for note in self.notes:
            if tag.lower() in [item.lower() for item in note.tags]:
                result.append(note)

        return result

    def get_all(self):
        return self.notes