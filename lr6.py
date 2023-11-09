import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Введіть довжину паролю: "))
    use_uppercase = input("Використовувати великі літери (так/ні)? ").lower() == "так"
    use_digits = input("Використовувати цифри (так/ні)? ").lower() == "так"
    use_special_chars = input("Використовувати спеціальні символи (так/ні)? ").lower() == "так"
    password = generate_password(password_length, use_uppercase, use_digits, use_special_chars)
    return password

def save_password(username, password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(f"{username}: {password}\n")

def view_passwords(filename="passwords.txt"):
    try:
        with open(filename, "r") as file:
            print("Збережені паролі:")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("Файл з паролями не знайдено.")

def delete_password(username, filename="passwords.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if not line.startswith(username + ":"):
                    file.write(line)
        print(f"Пароль для {username} був видалений.")
    except FileNotFoundError:
        print("Файл з паролями не знайдено.")

while True:
    print('\n Меню:')
    print('1. Створити новий пароль.')
    print('2. Створити та зберегти новий пароль.')
    print('3. Показати всі збережені паролі.')
    print("4. видалити пароль за ім'ям користувача.")
    print('5. Завершити виконання програми.')
    choice = input(' Виберіть що б ви хотіли зробити: ')
    if choice == str(1):
        password = main()
        print('Згенерований пароль:', password)
    elif choice == str(2):
        password = main()
        print('Згенерований пароль:', password)
        username = input("Введіть ім'я користувача, для якого зберегти цей пароль: ")
        save_password(username, password)
        print('Пароль збережено!')
    elif choice == str(3):
        view_passwords()
    elif choice == str(4):
        username = input("Введіть ім'я користувача для видалення: ")
        delete_password(username)
    elif choice == str(5):
        print('До побачення!')
        exit()
    else:
        print('Виникла помилка при введенні данних, будь ласка, спробуйте знову.')

