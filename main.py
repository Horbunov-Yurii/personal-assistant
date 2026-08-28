
import json
import pickle

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models.record import Record
from services.address_book import AddressBook
from models.note import Note
from services.note_book import NoteBook
from storage.storage import (
    export_to_json,
    import_from_json,
    load_data,
    save_data,
)


console = Console()

DATA_FILE = "storage/data.pkl"
EXPORT_FILE = "storage/backup.json"


# =========================
# LOAD DATA
# =========================

try:
    book, note_book = load_data(DATA_FILE)

except FileNotFoundError:
    book = AddressBook()
    note_book = NoteBook()

except (pickle.UnpicklingError, EOFError):
    console.print(
        "[yellow]Warning: Saved data is corrupted. "
        "Starting with empty data.[/yellow]"
    )
    book = AddressBook()
    note_book = NoteBook()


# =========================
# COMMANDS
# =========================

COMMANDS = {
    "add-contact": "Add a new contact",
    "find-contact": "Find a contact",
    "edit-contact": "Edit a contact",
    "delete-contact": "Delete a contact",
    "all-contacts": "Show all contacts",
    "birthdays": "Show upcoming birthdays",
    "add-note": "Add a new note",
    "find-note": "Find notes",
    "edit-note": "Edit a note",
    "delete-note": "Delete a note",
    "all-notes": "Show all notes",
    "find-by-tag": "Find notes by tag",
    "export-json": "Export contacts and notes to JSON",
    "import-json": "Import contacts and notes from JSON",
    "statistics": "Show application statistics",
    "help": "Show available commands",
    "exit": "Exit the assistant",
}


# =========================
# UI
# =========================

def show_welcome():
    console.print(
        Panel(
            "[bold]PERSONAL ASSISTANT[/bold]",
            title="Welcome",
            border_style="blue",
        )
    )


def show_menu():
    console.print("\n[bold blue]CONTACTS[/bold blue]")
    console.print("  add-contact     Add a new contact")
    console.print("  find-contact    Find a contact")
    console.print("  edit-contact    Edit a contact")
    console.print("  delete-contact  Delete a contact")
    console.print("  all-contacts    Show all contacts")
    console.print("  birthdays       Show upcoming birthdays")

    console.print("\n[bold green]NOTES[/bold green]")
    console.print("  add-note        Add a new note")
    console.print("  find-note       Find notes")
    console.print("  edit-note       Edit a note")
    console.print("  delete-note     Delete a note")
    console.print("  all-notes       Show all notes")
    console.print("  find-by-tag     Find notes by tag")

    console.print("\n[bold yellow]OTHER[/bold yellow]")
    console.print("  export-json     Export contacts and notes to JSON")
    console.print("  import-json     Import contacts and notes from JSON")
    console.print("  statistics      Show application statistics")
    console.print("  help            Show available commands")
    console.print("  exit            Exit the assistant")


def show_help():
    table = Table(
        title="Available Commands",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Command", style="bold")
    table.add_column("Description")

    for command, description in COMMANDS.items():
        table.add_row(command, description)

    console.print(table)


# =========================
# CONTACTS
# =========================

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    birthday = input("Enter birthday (DD.MM.YYYY): ").strip()

    try:
        record = Record(name)

        record.add_phone(phone)
        record.add_email(email)
        record.add_birthday(birthday)

        if book.add_record(record):
            console.print("[green]Contact added![/green]")
        else:
            console.print(
                "[red]Error: Contact with this name already exists.[/red]"
            )

    except ValueError as error:
        console.print(f"[red]Error: {error}[/red]")


def find_contact():
    query = input("Enter name, phone or email: ").strip()

    record = book.search(query)

    if record:
        table = Table(
            title="Contact Found",
            show_header=True,
            header_style="bold cyan",
        )

        table.add_column("Name")
        table.add_column("Phone")
        table.add_column("Email")
        table.add_column("Birthday")

        birthday = record.birthday

        if birthday and hasattr(birthday, "strftime"):
            birthday = birthday.strftime("%d.%m.%Y")

        table.add_row(
            str(record.name),
            ", ".join(str(phone) for phone in record.phones),
            str(record.email) if record.email else "-",
            str(birthday) if birthday else "-",
        )

        console.print(table)

    else:
        console.print("[red]Contact not found.[/red]")


def edit_contact():
    name = input("Enter contact name: ").strip()

    record = book.find(name)

    if record is None:
        console.print("[red]Contact not found.[/red]")
        return

    field = input(
        "What do you want to edit (phone/email)? "
    ).strip().lower()

    if field == "phone":
        old_phone = input("Enter old phone: ").strip()
        new_phone = input("Enter new phone: ").strip()

        try:
            result = book.edit_phone(
                name,
                old_phone,
                new_phone,
            )

            if result:
                console.print("[green]Phone updated![/green]")
            else:
                console.print("[red]Phone not found.[/red]")

        except ValueError as error:
            console.print(f"[red]Error: {error}[/red]")

    elif field == "email":
        old_email = input("Enter old email: ").strip()
        new_email = input("Enter new email: ").strip()

        try:
            result = book.edit_email(
                name,
                old_email,
                new_email,
            )

            if result:
                console.print("[green]Email updated![/green]")
            else:
                console.print("[red]Email not found.[/red]")

        except ValueError as error:
            console.print(f"[red]Error: {error}[/red]")

    else:
        console.print("[red]Unknown field.[/red]")


def delete_contact():
    name = input("Enter contact name: ").strip()

    record = book.find(name)

    if record is None:
        console.print("[red]Contact not found.[/red]")
        return

    field = input(
        "What do you want to delete (phone/email)? "
    ).strip().lower()

    if field == "phone":
        phone = input("Enter phone to delete: ").strip()

        result = book.remove_phone(name, phone)

        if result:
            console.print("[green]Phone deleted![/green]")
        else:
            console.print("[red]Phone not found.[/red]")

    elif field == "email":
        result = record.remove_email()

        if result:
            console.print("[green]Email deleted![/green]")
        else:
            console.print("[red]Email not found.[/red]")

    else:
        console.print("[red]Unknown field.[/red]")


def show_all_contacts():
    records = book.get_all()

    if not records:
        console.print("[yellow]No contacts found.[/yellow]")
        return

    table = Table(
        title="All Contacts",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Name")
    table.add_column("Phone")
    table.add_column("Email")
    table.add_column("Birthday")

    for record in records:
        birthday = record.birthday

        if birthday and hasattr(birthday, "strftime"):
            birthday = birthday.strftime("%d.%m.%Y")

        table.add_row(
            str(record.name),
            ", ".join(str(phone) for phone in record.phones),
            str(record.email) if record.email else "-",
            str(birthday) if birthday else "-",
        )

    console.print(table)


def show_birthdays():
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        console.print("[yellow]No upcoming birthdays.[/yellow]")
        return

    table = Table(
        title="Upcoming Birthdays",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Name")
    table.add_column("Birthday")

    for record, birthday in upcoming:
        table.add_row(
            str(record.name),
            birthday.strftime("%d.%m.%Y"),
        )

    console.print(table)


# =========================
# NOTES
# =========================

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()
    tags_input = input("Enter tags (comma separated): ").strip()

    tags = [
        tag.strip()
        for tag in tags_input.split(",")
        if tag.strip()
    ]

    note = Note(title, content, tags)
    note_book.add_note(note)

    console.print("[green]Note added![/green]")


def find_note():
    title = input("Enter note title: ").strip()

    note = note_book.find(title)

    if note:
        table = Table(
            title="Note Found",
            show_header=True,
            header_style="bold green",
        )

        table.add_column("Title")
        table.add_column("Content")
        table.add_column("Tags")

        table.add_row(
            str(note.title),
            str(note.content),
            ", ".join(str(tag) for tag in note.tags)
            if note.tags
            else "-",
        )

        console.print(table)

    else:
        console.print("[red]Note not found.[/red]")


def edit_note():
    title = input("Enter note title: ").strip()
    new_content = input("Enter new content: ").strip()

    result = note_book.edit(title, new_content)

    if result:
        console.print("[green]Note updated![/green]")
    else:
        console.print("[red]Note not found.[/red]")


def delete_note():
    title = input("Enter note title: ").strip()

    result = note_book.delete(title)

    if result:
        console.print("[green]Note deleted![/green]")
    else:
        console.print("[red]Note not found.[/red]")


def show_all_notes():
    notes = note_book.get_all()

    if not notes:
        console.print("[yellow]No notes found.[/yellow]")
        return

    table = Table(
        title="All Notes",
        show_header=True,
        header_style="bold green",
    )

    table.add_column("Title")
    table.add_column("Content")
    table.add_column("Tags")

    for note in notes:
        table.add_row(
            str(note.title),
            str(note.content),
            ", ".join(str(tag) for tag in note.tags)
            if note.tags
            else "-",
        )

    console.print(table)


def find_note_by_tag():
    tag = input("Enter tag: ").strip()

    notes = note_book.find_by_tag(tag)

    if not notes:
        console.print(
            "[red]No notes found with this tag.[/red]"
        )
        return

    table = Table(
        title=f"Notes with tag: {tag}",
        show_header=True,
        header_style="bold green",
    )

    table.add_column("Title")
    table.add_column("Content")
    table.add_column("Tags")

    for note in notes:
        table.add_row(
            str(note.title),
            str(note.content),
            ", ".join(str(tag) for tag in note.tags)
            if note.tags
            else "-",
        )

    console.print(table)


# =========================
# STATISTICS
# =========================

def show_statistics():
    records = book.get_all()
    notes = note_book.get_all()

    total_contacts = len(records)
    total_notes = len(notes)

    contacts_with_phone = sum(
        1 for record in records if record.phones
    )

    contacts_with_email = sum(
        1 for record in records if record.email
    )

    contacts_with_birthday = sum(
        1 for record in records if record.birthday
    )

    notes_with_tags = sum(
        1 for note in notes if note.tags
    )

    total_tags = sum(
        len(note.tags) for note in notes
    )

    table = Table(
        title="Application Statistics",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("Metric")
    table.add_column("Value", justify="right")

    table.add_row(
        "Contacts",
        str(total_contacts),
    )

    table.add_row(
        "Notes",
        str(total_notes),
    )

    table.add_row(
        "Contacts with phone",
        str(contacts_with_phone),
    )

    table.add_row(
        "Contacts with email",
        str(contacts_with_email),
    )

    table.add_row(
        "Contacts with birthday",
        str(contacts_with_birthday),
    )

    table.add_row(
        "Notes with tags",
        str(notes_with_tags),
    )

    table.add_row(
        "Total tags",
        str(total_tags),
    )

    console.print(table)


# =========================
# JSON IMPORT / EXPORT
# =========================

def export_json():
    try:
        export_to_json(
            book,
            note_book,
            EXPORT_FILE,
        )

        console.print(
            f"[green]Data exported successfully to "
            f"{EXPORT_FILE}![/green]"
        )

    except OSError as error:
        console.print(
            f"[red]Error: Could not export data: {error}[/red]"
        )


def import_json():
    global book, note_book

    filename = input(
        "Enter JSON file path "
        "(default: storage/backup.json): "
    ).strip()

    if not filename:
        filename = EXPORT_FILE

    try:
        imported_book, imported_note_book = import_from_json(
            filename
        )

        book = imported_book
        note_book = imported_note_book

        save_data(
            (book, note_book),
            DATA_FILE,
        )

        console.print(
            "[green]Data imported successfully![/green]"
        )

    except FileNotFoundError:
        console.print(
            f"[red]Error: File not found: {filename}[/red]"
        )

    except json.JSONDecodeError:
        console.print(
            "[red]Error: Invalid JSON file.[/red]"
        )

    except (KeyError, TypeError, ValueError) as error:
        console.print(
            f"[red]Error: Invalid data format: {error}[/red]"
        )

    except OSError as error:
        console.print(
            f"[red]Error: Could not read file: {error}[/red]"
        )


# =========================
# COMMAND HANDLER
# =========================

def handle_command(command):
    if command == "exit":
        try:
            save_data(
                (book, note_book),
                DATA_FILE,
            )

            console.print(
                "[green]Data saved successfully![/green]"
            )

        except OSError as error:
            console.print(
                f"[red]Error: Could not save data: {error}[/red]"
            )

        return False

    if command == "help":
        show_help()

    elif command == "add-contact":
        add_contact()

    elif command == "find-contact":
        find_contact()

    elif command == "edit-contact":
        edit_contact()

    elif command == "delete-contact":
        delete_contact()

    elif command == "all-contacts":
        show_all_contacts()

    elif command == "birthdays":
        show_birthdays()

    elif command == "add-note":
        add_note()

    elif command == "find-note":
        find_note()

    elif command == "edit-note":
        edit_note()

    elif command == "delete-note":
        delete_note()

    elif command == "all-notes":
        show_all_notes()

    elif command == "find-by-tag":
        find_note_by_tag()

    elif command == "statistics":
        show_statistics()

    elif command == "export-json":
        export_json()

    elif command == "import-json":
        import_json()

    else:
        console.print(
            f"[red]Unknown command: {command}[/red]"
        )

    return True


# =========================
# MAIN
# =========================

def main():
    show_welcome()
    show_menu()

    try:
        while True:
            command = input(
                "\nEnter command: "
            ).strip().lower()

            if not handle_command(command):
                console.print("\nGoodbye!")
                break

    except KeyboardInterrupt:
        console.print(
            "\n\n[yellow]Goodbye![/yellow]"
        )

    except Exception as error:
        console.print(
            f"\n[red]Unexpected error: {error}[/red]"
        )


if __name__ == "__main__":
    main()
