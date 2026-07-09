import time
import random

name = None
password = None
plasma = random.randint(1, 10)
selected_command = None
is_registered = False
bit = 31

for bit in range(1, 11):
    print(bit * 3)

print("Добро пожаловать в Terminal Classic!")
time.sleep(1)
print("Необходимо зарегистрироваться.")
time.sleep(1)

def register():
    global name, password, is_registered
    name = input("Создайте имя: ")
    password = input("Создайте пароль: ")
    is_registered = True
    print(f"Пользователь {name} создан!")

def show_commands():
    print("==============")
    print("Доступные команды: ")
    print("1. whoami - показывает текущего пользователя.")
    print("2. plasma - генерирует случайное число.")
    print("3. bit - показывает много чисел.")
    print("4. help - показывает команды.")
    print("5. exit - закрывает текущую сессию терминала.")
    print("==============")

def game_loop():
    global name, plasma, bit

    while True:
        cmd_comm = input("Выберите команду (1-5): ").strip()

        if cmd_comm == "1":
            print(name)
        elif cmd_comm == "2":
            print(plasma)
        elif cmd_comm == "3":
            print(bit)
        elif cmd_comm == "4":
            show_commands()
        elif cmd_comm == "5":
            print("Выход из текущей сессии...")
            time.sleep(1)
            print("Закрытие файлов пользователя...")
            time.sleep(1)
            print(f"Выход осуществлён, {name}.")
            break
        else:
            print("Неизвестная команда. Введи 4 для помощи.")

# --- ЗАПУСК ---
register()

if is_registered:
    print(f"Добро пожаловать, {name}!")
    time.sleep(1)
    show_commands()
    game_loop()
else:
    print("Вы ещё не зарегистрированы!")
