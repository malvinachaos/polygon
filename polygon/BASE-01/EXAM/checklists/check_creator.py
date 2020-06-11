#! /usr/bin/python3
from os import system as S
import pickle
S("clear")
# ---------------------------[GREETINGS]------------------------------------- #
'''
    Даный фрагмент кода приветствует пользователя и создаёт список чек-листов,
    которые есть в той же директории, что и сама программа.
'''
print("""
    CHECK-LIST CREATOR v0.2
        Made by MalvinaChaos

""")
S("sleep 2s")
S("clear")

CHECKLIST = ''
S("ls *.data > list")
with open("list", 'r') as F:
    CHECKLIST = F.read()

CHECKLIST = CHECKLIST.split('\n')
CHECKLIST.pop()
S("rm list")

# ---------------------------[FUNCTIONS]------------------------------------- #
# Выбирает нужный файл из заранее сгенерированного списка
def choose_checklist():
    global CHECKLIST
    while True:
        message("Введите цифру чек-листа: ")
        for i, item in enumerate(CHECKLIST):    # выводит список (0) FST.data
            print('\t(', i,') ', item, sep='')  # к примеру      (1) SNВ.data
        c = input(": ")

        if not c.isdigit():
            message("Вы неверно ввели даные!!") # Следующие два блока -- 
            S("sleep 1s")                       # проверка на правильность
            S("clear")                          # ввода
            continue
        else: c = int(c)

        if c > len(CHECKLIST)-1:
            message("Вы неверно ввели даные!!")
            S("sleep 1s")
            S("clear")
            continue
        else: return CHECKLIST[c]

# Анимация вывода текста
def message(msg):
    for i in range(len(msg)):
        print(msg[:i], end='\r')
        S("sleep 0.01s")
    S("sleep 0.02s")
    print()

# Чтение из файла
def read_data():
    S("clear")
    choose = choose_checklist()
    Data = []
    with open(choose, 'rb') as f:
        Data = pickle.load(f)
    message("Прочитано ")
    return Data

# Вывод на экран
def show_data(Data):
    S("clear")
    print("-"*134)
    print("№  | сложность | оценка | ошибки\
                                     | что делать?")
    print("-"*134)
    for i, item in enumerate(Data):
        to_load = [item.get("№"), item.get("сложность"), item.get("оценка"),\
            item.get("ошибка"), item.get("что делать?")]
        print("{0[0]:2} | {0[1]:9} | {0[2]:6} | {0[3]:34}   {0[4]:24}".format(to_load))
        print("-"*134)
    c = input("\n. . . ENTER . . .")

# Запись в файл
def write_data(Data):
    S("clear")
    c = ''
    while True:
        message("Введите имя файла: ")
        c = input(": ")
        if ".data" not in c:
            c = c + ".data"
        if c in CHECKLIST:
            message("Такой файл уже существует! Перезаписать его? ")
            choose = input("[Y/N]: ")
            if choose.upper() == 'Y':
                break
            else:
                continue
        S("clear")
        break

    with open(c, 'wb') as f:
        pickle.dump(Data, f)
    
    message("Записано")

# Запись и редактирование в список
def edit_data(Data):
    # Добавляет запись
    def add_record():
        num = input("Номер задания(число): ")
        complexity = input("Сложность(easy/middle/hard): ")
        mark = input("Оценка(число): ")
        mistake = input("В чём заключалась ошибка?: ")
        suggest = input("Что надо сделать, чтобы её устранить?: ")
        if num.isdigit() and complexity in ("easy", "middle", "hard"):
            return {
                        "№":num,\
                        "сложность":complexity,\
                        "оценка":mark,\
                        "ошибка":mistake,\
                        "что делать?":suggest\
                        }
        else:
            message("Вы неверно ввели данные ")
            return

    while True:
        S("clear")
        message("Добавить, редактировать или удалить запись??")
        choice = input("add/edit/remove: ")
        if choice not in ("add", "edit", "remove"):
            message("Такой опции нетт")
            continue
        elif choice == "add":
            a = add_record()
            if type(a) == dict:
                Data.append(a)
        elif choice == "edit":
            message("Введите номер записи, (их всего) {}  ".format(len(Data)))
            n = int(input(": ")) - 1
            Data[n] = add_record()
        elif choice == "remove":
            message("Введите номер записи, (их всего) {}  ".format(len(Data)))
            n = int(input(": ")) - 1
            Data.pop(n)
        message("Создать ещё одну запись??")
        choice = input("[Y/N]: ")
        if choice.upper() == "Y":
            continue
        else:
            return Data


# ---------------------------[MAIN]------------------------------------------ #

S("whoami > name")                      # 5 строчек только для того, чтобы
USER = '???'                            # вывести имя польхователя на экран
with open("name", 'r') as F:
    USER = F.read()
S("rm name")

message("Привет, " + str(USER)[:-1] + "!!")

c = ''
data = []
while True:
    message("Что вы хотите сделать? ")
    c = input("""
 (r) Прочитать файл
 (w) Записать в файл
 (e) Редактировать данные
 (s) Просмотреть все данные
 (q) Выйти из программы
 : """)
    if c == 'r':
        data = read_data()
    elif c == 'w' and data != []:
        write_data(data)
    elif c == 'e':
        data = edit_data(data)
    elif c == 's' and data != []:
        show_data(data)
    elif c == 'q':
        break
    else:
        message(". . . ")
        message("Такого пункта нет ")
        S("sleep 1s")
    S("clear")

