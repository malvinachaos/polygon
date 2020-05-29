#! /usr/bin/python3
from os import system as S
import pickle
S("clear")
# ---------------------------[GREETINGS]------------------------------------- #
print("""
    CHECK-LIST CREATOR v0.1
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
# Выбирает нужный файл из списка
def choose_checklist():
    global CHECKLIST
    while True:
        message("Введите цифру чек-листа: ")
        for i, item in enumerate(CHECKLIST):
            print('\t(', i,') ', item, sep='')
        c = input(": ")

        if not c.isdigit():
            message("Вы неверно ввели даные!!")
            S("sleep 1s")
            S("clear")
            continue
        else: c = int(c)

        if c > len(CHECKLIST)-1:
            message("Вы неверно ввели даные!!")
            S("sleep 1s")
            S("clear")
            continue
        else: return CHECKLIST[c]

# "Специальный" вывод текста
def message(msg):
    for i in range(len(msg)):
        print(msg[:i], end='\r')
        S("sleep 0.05s")
    S("sleep 0.2s")
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
    print("-"*77)
    print("№ | сложность | оценка | ошибки           | что делать?")
    print("-"*77)
    for i, item in enumerate(Data):
        to_load = [item.get("№"), item.get("сложность"), item.get("оценка"),\
            item.get("ошибка"), item.get("что делать?")]
        print("{0[0]} | {0[1]:9} | {0[2]:6} | {0[3]:16} | {0[4]:24}".format(to_load))
        print("-"*77)
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
            message("Такой файл уже существует! Перезаписать существующий файл??")
            choose = input("[Y/N]: ")
            if choose.upper() == 'Y':
                break
            else:
                continue
        S("clear")
        break

    with open(c, 'wb') as f:
        pickle.dump(Data, f)

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
            return {
                        "№":'0',\
                        "сложность":'none',\
                        "оценка":'0',\
                        "ошибка":'none',\
                        "что делать?":'none'\
                        }

    while True:
        S("clear")
        message("Добавить или редактировать существующую запись??")
        choice = input("add/edit: ")
        if choice not in ("add", "edit"):
            message("Такой опции нетт")
            continue
        elif choice == "add":
            Data.append(add_record())
        elif choice == "edit":
            message("Введите номер записи, (их всего) {}  ".format(len(Data)))
            n = int(input(": ")) - 1
            Data[n] = add_record()
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