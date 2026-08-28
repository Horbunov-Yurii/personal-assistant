# Personal Assistant

Консольний персональний асистент на Python для керування контактами та нотатками.

Програма дозволяє зберігати контактну інформацію, працювати з нотатками, знаходити найближчі дні народження, імпортувати та експортувати дані у форматі JSON, переглядати статистику та зберігати всі дані між запусками програми.

## Features

### Contacts

* Додавання нового контакту
* Пошук контакту за ім'ям, телефоном або email
* Редагування номера телефону
* Редагування email
* Видалення номера телефону
* Видалення email
* Перегляд усіх контактів
* Перегляд найближчих днів народження
* Валідація номера телефону
* Валідація email
* Валідація дати народження

### Notes

* Додавання нотаток
* Пошук нотатки за назвою
* Редагування нотатки
* Видалення нотатки
* Перегляд усіх нотаток
* Пошук нотаток за тегом

### Import / Export

Програма підтримує імпорт та експорт контактів і нотаток у форматі JSON.

Доступні команди:

```text
export-json
import-json
```

За замовчуванням для експорту та імпорту використовується файл:

```text
storage/backup.json
```

### Statistics

Програма має команду для перегляду статистики:

```text
statistics
```

Статистика містить:

* загальну кількість контактів;
* кількість контактів з телефоном;
* кількість контактів з email;
* кількість контактів з днем народження;
* загальну кількість нотаток;
* кількість нотаток з тегами;
* загальну кількість тегів.

### Rich CLI

Для покращення консольного інтерфейсу використовується бібліотека `rich`.

Програма використовує:

* кольорові повідомлення;
* панель привітання;
* таблицю контактів;
* таблицю нотаток;
* таблицю статистики;
* таблицю доступних команд.

### Data Persistence

Дані програми автоматично зберігаються у файл:

```text
storage/data.pkl
```

Для збереження використовується стандартний модуль Python `pickle`.

При запуску програма автоматично завантажує збережені контакти та нотатки.

Якщо файл сховища відсутній, програма створює порожню адресну книгу та сховище нотаток.

Якщо файл пошкоджений, програма повідомляє користувача та запускається з порожніми даними.

Файл `storage/data.pkl` не зберігається у Git та доданий до `.gitignore`.

## Technologies

* Python
* `pickle`
* `json`
* `datetime`
* `re`
* `email-validator`
* `rich`
* `unittest`

## Project Structure

```text
personal-assistant/
│
├── app/
│   └── __init__.py
│
├── contacts/
│   └── __init__.py
│
├── models/
│   ├── birthday.py
│   ├── email.py
│   ├── name.py
│   ├── note.py
│   ├── phone.py
│   └── record.py
│
├── notes/
│   └── __init__.py
│
├── services/
│   ├── address_book.py
│   └── note_book.py
│
├── storage/
│   ├── __init__.py
│   └── storage.py
│
├── tests/
│   ├── test_address_book.py
│   └── test_note_book.py
│
├── utils/
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd personal-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

macOS / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python3 main.py
```

Після запуску програма покаже список доступних команд.

## Available Commands

### Contacts

```text
add-contact
find-contact
edit-contact
delete-contact
all-contacts
birthdays
```

### Notes

```text
add-note
find-note
edit-note
delete-note
all-notes
find-by-tag
```

### Other

```text
export-json
import-json
statistics
help
exit
```

## Examples

### Add Contact

```text
Enter command: add-contact

Enter name: John
Enter phone: 0501234567
Enter email: john@example.com
Enter birthday (DD.MM.YYYY): 28.08.1990

Contact added!
```

### Add Note

```text
Enter command: add-note

Enter note title: Shopping
Enter note content: Buy milk
Enter tags (comma separated): shopping, home

Note added!
```

### View Contacts

```text
Enter command: all-contacts

                   All Contacts
┏━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Name ┃ Phone      ┃ Email             ┃ Birthday   ┃
┡━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ John │ 0501234567 │ john@example.com   │ 28.08.1990 │
└──────┴────────────┴───────────────────┴────────────┘
```

### View Statistics

```text
Enter command: statistics

      Application Statistics
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric                 ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Contacts               │     1 │
│ Notes                  │     1 │
│ Contacts with phone    │     1 │
│ Contacts with email    │     1 │
│ Contacts with birthday │     1 │
│ Notes with tags        │     1 │
│ Total tags             │     2 │
└────────────────────────┴───────┘
```

### Export Data

```text
Enter command: export-json

Data exported successfully to storage/backup.json!
```

### Import Data

```text
Enter command: import-json

Enter JSON file path (default: storage/backup.json):
Data imported successfully!
```

## Testing

Для тестування використовується стандартний модуль Python `unittest`.

Запустити всі тести:

```bash
python3 -m unittest discover -s tests -v
```

Поточний набір тестів перевіряє основну функціональність `AddressBook` та `NoteBook`.

Результат успішного запуску:

```text
----------------------------------------------------------------------
Ran 15 tests in 0.003s

OK
```

### AddressBook Tests

Перевіряються:

* додавання контакту;
* дублювання контакту;
* пошук за ім'ям;
* пошук за телефоном;
* пошук за email;
* редагування телефону;
* редагування email;
* видалення телефону;
* отримання всіх контактів.

### NoteBook Tests

Перевіряються:

* додавання нотатки;
* пошук нотатки;
* редагування нотатки;
* видалення нотатки;
* пошук нотаток за тегом;
* отримання всіх нотаток.

## Error Handling

Програма обробляє основні помилки користувача та системи:

* неправильний номер телефону;
* неправильний email;
* неправильну дату народження;
* пошук неіснуючого контакту;
* пошук неіснуючої нотатки;
* невідому команду;
* відсутній файл сховища;
* пошкоджений файл `data.pkl`;
* відсутній JSON-файл;
* некоректний JSON-файл;
* некоректну структуру імпортованих даних;
* помилки під час збереження даних;
* помилки під час експорту даних;
* переривання програми через `Ctrl+C`.

## Development

Проєкт побудований з розділенням відповідальності між моделями, сервісами, сховищем та консольним інтерфейсом.

Основні компоненти:

* `models/` — моделі даних;
* `services/` — бізнес-логіка роботи з контактами та нотатками;
* `storage/` — збереження та імпорт/експорт даних;
* `tests/` — автоматизовані тести;
* `main.py` — консольний інтерфейс та обробка команд.

## Author

Personal Assistant project created as a Python learning project.
