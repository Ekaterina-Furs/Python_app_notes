import json
from datetime import datetime
import os


def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", 'r') as file:
            notes = json.load(file)
        return notes
    return []


def save_notes(notes):
    with open("notes.json", 'w') as file:
        json.dump(notes, file, indent=2)


def add_note(title, body):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print(f"Добавлена новая заметка {note_id} .")


def list_notes():
    notes = load_notes()
    if not notes:
        print("Нет сохраненных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(f"Тело заметки: {note['body']}")
            print("-" * 60)


def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print(f"Заметка под номером {note_id} отредактирована.")
            return
    print(f"Заметка под номером {note_id} не найдена.")


def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print(f"Заметка под номером {note_id} удалена.")
            return
    print(f"Заметка под номером {note_id} не найдена.")


def user_interface():
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            edit_note(note_id, title, body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Необходимо выбрать действие из списка.")


user_interface()