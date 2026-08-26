from rich.console import Console
from rich.panel import Panel

from models.record import Record
from services.address_book import AddressBook


console = Console()
book = AddressBook()


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
    "help": "Show available commands",
    "exit": "Exit the assistant",
}


def show_welcome():
    console.print(
        Panel(
            "PERSONAL ASSISTANT",
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

    console.print("\n[bold yellow]OTHER[/bold yellow]")
    console.print("  help            Show available commands")
    console.print("  exit            Exit the assistant")


def show_help():
    console.print("\n[bold]Available commands:[/bold]")

    for command, description in COMMANDS.items():
        console.print(f"  {command:<16} {description}")


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
        console.print("[green]Found:[/green]")
        console.print(record)
    else:
        console.print("[red]Contact not found.[/red]")


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


def show_all_contacts():
    records = book.get_all()

    if not records:
        console.print("No contacts found.")
        return

    console.print("\n[bold]All contacts:[/bold]")

    for record in records:
        console.print(record)


def show_birthdays():
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        console.print("No upcoming birthdays.")
        return

    console.print("\n[bold]Upcoming birthdays:[/bold]")

    for record, birthday in upcoming:
        console.print(
            f"{record.name}: {birthday.strftime('%d.%m.%Y')}"
        )


def handle_command(command):
    if command == "exit":
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

    elif command in COMMANDS:
        console.print(f"You entered: {command}")

    else:
        console.print(f"Unknown command: {command}")

    return True


def main():
    show_welcome()
    show_menu()

    while True:
        command = input("\nEnter command: ").strip().lower()

        if not handle_command(command):
            console.print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()