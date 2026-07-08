import time
import random
                                    
name = None
password = None
plasma = random.randint(1,10)
selected_command = None
is_registered = False

print("Добро пожаловать в Terminal Classic!")
time.sleep(1)
print("Необходимо зарегистрироваться.")
time.sleep(1)

def register():
  global name,password, is_registered 
  name = input("Создайте имя:")
  password = input("Создайте пароль:")
  is_registered = True
  print(f"Пользователь {name} создан!")
  
  
  print("Необходимо выполнить логин.")
  time.sleep(2)
  
  def login():
    global name,password, is_registered
    print("== ВХОД==")
    name_login = input("Введите имя:")
    pass_login = input("Введите пароль.")
    if name_login == name and pass_login == password:
        print(f"С возвращением, {name}!")
        return True
    else:
        print("Неверный логин или пароль!")
        return False
        
   
     
   
        
        
