from rich.console import Console
from rich.panel import Panel


console = Console()


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


def handle_command(command):
    if command == "exit":
        return False

    if command == "help":
        show_help()
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