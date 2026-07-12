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
    print("5. time - закрывает текущую сессию терминала.")
    print("6. exit - показывает теущее время сессии.")

def game_loop():
    global name, plasma, bit

    while True:
        cmd_comm = input("Выберите команду (1-5): ").strip()

        if cmd_comm == "1":
            print(name)
        elif cmd_comm == "2":
            print(plasma)
        elif cmd_comm == "3":
            for i in range(1, 11):
                print(i * 3, end=" ")
            print()
        elif cmd_comm == "4":
            show_commands()
        elif cmd_comm == "5":
            print(f"Время: {time.strftime('%H: %M')} ")
            print(f"Месяц: {time.strftime('%B')} ")
        elif cmd_comm == "6":
            print("Выход из текущей сессии.. ")
            time.sleep(3)
            print(f"Выход осуществлен {name}. ")
            break
        else:
            print("Неизвестная команда, введите 4 для подробностей.")

# --- ЗАПУСК ---
register()

if is_registered:
    print(f"Добро пожаловать, {name}!")
    time.sleep(1)
    show_commands()
    game_loop()
else:
    print("Вы ещё не зарегистрированы!")
