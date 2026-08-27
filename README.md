# Personal Assistant

Консольний персональний асистент на Python для керування контактами та нотатками.

Програма дозволяє зберігати контактну інформацію, працювати з нотатками, знаходити найближчі дні народження та зберігати всі дані між запусками програми.

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

### Data persistence

Дані програми автоматично зберігаються у файл:

```text
storage/data.pkl
```

Для збереження використовується стандартний модуль Python `pickle`.

При запуску програма автоматично завантажує збережені контакти та нотатки.

Якщо файл сховища відсутній, програма створює порожню адресну книгу та сховище нотаток.

Якщо файл пошкоджений, програма не завершується з помилкою, а повідомляє користувача та запускається з порожніми даними.

## Technologies

* Python
* `pickle`
* `datetime`
* `re`
* `email-validator`
* `rich`

## Project structure

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

## Run the application

```bash
python3 main.py
```

Після запуску програма покаже список доступних команд.

## Available commands

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
help
exit
```

## Example

```text
Enter command: add-contact

Enter name: John
Enter phone: 380501111111
Enter email: john@example.com
Enter birthday (DD.MM.YYYY): 28.08.1990

Contact added!
```

Після перезапуску програми збережені дані будуть автоматично завантажені.

## Error handling

Програма обробляє основні помилки користувача та системи:

* неправильний номер телефону;
* неправильний email;
* неправильну дату народження;
* пошук неіснуючого контакту;
* пошук неіснуючої нотатки;
* невідому команду;
* відсутній файл сховища;
* пошкоджений файл `data.pkl`;
* помилки під час збереження даних;
* переривання програми через `Ctrl+C`.

## Author

Personal Assistant project created as a Python learning project.
