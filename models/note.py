class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags or []

    def __str__(self):
        tags = ", ".join(self.tags) if self.tags else "Not specified"

        return f"Title: {self.title}\n" f"Content: {self.content}\n" f"Tags: {tags}"


if __name__ == "__main__":
    note = Note(
        "Shopping",
        "Buy milk and bread",
        ["shopping", "home"],
    )

    print(note)
