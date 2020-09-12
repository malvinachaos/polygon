#! /usr/bin/python3
from os import getcwd, getlogin, mkdir, listdir
from os import system as S
from os.path import abspath, isdir
from time import sleep


S("clear||cls")

if not isdir(".base_01_files"):
    mkdir(".base_01_files")

PATH = getcwd()
USER = "marina"
FILE = "/.base_01_files"
PATH_FILE = listdir(PATH+FILE)

# ---------------------------[Запуск программы]--------------------------------
# Титульный экран
print("\n\tBASE-01 v0.2.0\n\n\tMADE BY LAZY DRAGON!\n\n\n\
Создан 29.03.2020\nПоследнее обновление 22.06.2020")

sleep(2)
S("clear")

# setup

import logo
sleep(2)
S("clear")
# ---------------------------[Блок математических подпрограм]------------------
def number_system():
    ''' Эта функция переводит целые положительные числа с основанием по модулю
        не более 16.
    '''
    NUM = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', \
            'D','E', 'F')

    # M - число, N - основание. Эта функция переводит из любой сс в десятичную
    def n_to_dec(M, N, NUM):
        # Защита
        if M == '0':
            return 0
        if N == 1:
            print("Информации с таким основанием не будет существовать.")
            return 0
        elif N == 0:
            print("Основание не может быть равно нулю")
            return 0
        elif N < 0:
            print("Основание не может быть отрицательным")
            return 0
        elif N > 16:
            print("Основание не может быть больше 16")

        # Сам алгоритм перевода
        l, S = len(M)-1, 0
        for i, item in enumerate(M):
            S += NUM.index(item)*N**l
            l -= 1
        return S

    def dec_to_ns(M, N, NUM):
        if N in (0, 1):
            print("Невозможно перевести число")
            return 0
        result = ''
        while M > 0:
            result += NUM[M%N]
            M //= N
        return ''.join(reversed(list(result)))

    m, n = input("Введите число: "), int(input("Введите его основание: "))
    m = m.upper()
    new_ns = int(input("Введите систему счисление, в котороу хотите перевести число: "))
    print(dec_to_ns(n_to_dec(m, n, NUM), new_ns, NUM))

def square_table():
    ''' Рисует таблицу квадратов от 10 до 99
    '''
    # Цвета G -- зелёный, B -- синий, C -- голубой, reset -- сброс цвета
    G , B, C, reset= '\033[42m', '\033[44m', '\033[46m', '\033[0m'

    # Вывод шапки таблицы
    numbers =  " "*5 + (" "*4).join([str(x+1) for x in range(0, 9)])
    print(G + numbers, reset)

    # Вывод содержимого таблицы
    for i in range(1, 10):
        print(B + "{:<2,d}".format(i) + reset, end='')
        for j in range(1, 10):
            print(C + "{:>4d}".format((j+i*10)**2), reset, end='')
        print()

def typical_square():
    ''' Решает уравнения типа ax^2 + bx + c = 0
    '''
    def number_input(num):
        if num[0] == '-':
            if num[1:].isdigit():
                return int(num)
        elif num.isdigit():
                return int(num)
        else:
            return 1

    a = input("Введите a: ")
    if a == '0':
        print("это уже не квадратное уравнение, лмао\n\n")
        return
    a = number_input(a)

    b, c = number_input(input("Введите b: ")), number_input(input("Введите c: "))

    D = b**2 + 4*a*c*(-1)
    if D < 0:
        print("Дискриминант отрицателен (", D, ")", sep='')
        return
    elif D == 0:
        print("Корень этого уравнения:", (-b)/(2*a))
    else:
        x1, x2 = ((-b) - D**(1/2))/(2*a), ((-b) + D**(1/2))/(2*a)
        print(f"Корни этого уравнения: {x1} и {x2}\nДискриминант: {D}")


# ---------------------------[Блок редактора текста]---------------------------
def psycho():
    ''' Данная программа редактирует текст из файла или с клавиатуры.
    '''
    # ------------------[Блок функций]----------------------
    #### [Алгоритмы редактирования]

    def jump(txt):
        ''' ПрЫгАюЩиЙ ТеКсТ '''
        tnt, flg = '', True
        for i, item in enumerate(txt):
            if flg:
                tnt += item.upper()
                flg = False
                continue
            else:
                tnt += item.lower()
                flg = True
        return tnt

    def remove_punctuation_signs(txt):
        ''' Убирает знаки препинания '''
        tnt = ''
        for i, item in enumerate(txt):
            if item.isalnum() or item.isspace():
                tnt += item
        return tnt

    def Dramatic(a):
        ''' Между слов ставит многоточия '''
        a, b = a.lower(), ""
        for i, item in enumerate(a):
            if item.isalnum() or (item in "\n\t "):
                b += item
        b = b.split()
        b = "... ".join(b) + "..."
        return b

    def epic(txt):
        ''' Делает текст капсом и разделяет пробелами буквы '''
        txt = txt.upper()
        txt = txt.split()
        tnt = ['']

        for i, item in enumerate(txt):
            for j, item in enumerate(txt[i]):
                tnt[i] += item + ' '
            tnt[i] += ' '
            tnt.append('')

        return ''.join(tnt)

    def main(txt):
        global PATH, FILE
        choose = input("""Введите алгоритм редактирования:
	* 0 -- Делает буквы прописными через одну
	* 1 -- Убирает знаки препинания
	* 2 -- Между слов ставит многоточия
	* 3 -- Делает текст капсом и разделяет пробелами буквы
    : """)

        if choose == '0':
            txt = jump(txt)
        elif choose == '1':
            txt = remove_punctuation_signs(txt)
        elif choose == '2':
            txt = Dramatic(txt)
        elif choose == '3':
            txt = epic(txt)

        # Сохранить в файл?
        ch = input("Сохранить в файл?[Y/N]: ")

        if ch == 'Y':
            name = input("Введите имя файла: ")
            name = PATH+FILE+'/'+name
            save(txt, name)

        print(txt)
        input("...")

    def save(txt, tnt):
        global FILE, PATH
        if '.txt' not in tnt:
            tnt += '.txt'
        tnt = FILE + PATH + "/" + tnt
        with open(tnt, 'w') as F:
            F.write(txt)

    def FILE():
        global PATH_FILE, FILE, PATH
        tnt = ''
        files = [x for x in PATH_FILE if ".txt" in x]
        print("Введите номер файла ")
        for i, item in enumerate(files):
            print(f" ({i+1}) - {item}")

        while True:
            tnt = int(input(": ")) - 1
            text = ''
            if tnt < len(files):
                text = PATH + FILE + "/" + files[tnt]
                break
            else:
                print("Вы неверно ввели данные! ")

        with open(text, 'r') as F:
            txt = F.read()
        main(txt)

    def KEYBOARD():
        stroka = input("Введите строку: ")
        main(stroka)

    while True:
        print("""
 * FILE -- Редактирование из файла
 * KEYB -- Редактирование с клавиатуры
 * q    -- Выход
        """)
        choose = input(": ")

        if choose.upper() == 'FILE': FILE()
        elif choose.upper() == 'KEYB': KEYBOARD()
        elif choose.lower() == 'q': break

# ---------------------------[Блок подрограммы создания чек-листа]-------------
def check_creator():
    ''' Данная программа создаёт и читает чек-листы '''
    import pickle
    # -------------[GREETINGS]------------------ #
    CHECKLIST = [x for x in PATH_FILE if ".data" in x]

    # -------------[FUNCTIONS]------------------ #
    def choose_checklist(CHECKLIST):
        ''' Выбирает нужный файл из заранее сгенерированного списка '''
        if len(CHECKLIST) == 0:
            message("Нет файлов ")
            return 0

        while True:
            message("Введите цифру чек-листа: ")
            for i, item in enumerate(CHECKLIST):
                print('\t(', i,') ', item, sep='')
            c = input(": ")

            if not c.isdigit():
                message("Вы неверно ввели даные!!")
                sleep(1)
                S("clear")
                continue
            else: c = int(c)

            if c > len(CHECKLIST)-1:
                message("Вы неверно ввели даные!!")
                sleep(1)
                S("clear")
                continue
            else: return CHECKLIST[c]

    def read_data():
        ''' Чтение из файла '''
        choose = choose_checklist(CHECKLIST)
        if choose == 0:
            return []

        choose = PATH + FILE + "/" + choose
        Data = []
        with open(choose, 'rb') as f:
            Data = pickle.load(f)
        message("Прочитано ")
        return Data

    def show_data(Data):
        ''' Вывод на экран '''
        for i, item in enumerate(Data):
            to_load = [item.get("№"), item.get("сложность"), \
                    item.get("оценка"), item.get("ошибка"), \
                    item.get("что делать?")]
            print("{0[0]} | {0[1]} | {0[2]} | {0[3]} | {0[4]}".format(to_load))
        c = input("\n. . . ENTER . . .")

    def write_data(Data, CHECKLIST):
        ''' Запись в файл '''
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
            break

        c = PATH+FILES+"/"+c
        with open(c, 'wb') as f:
            pickle.dump(Data, f)

        message("Записано")

    def edit_data(Data):
        ''' Запись и редактирование в список '''
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

    # ----------------[MAIN]------------------- #
    message("Привет, " + USER + "!!")

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
            write_data(data, CHECKLIST)
        elif c == 'e':
            data = edit_data(data)
        elif c == 's' and data != []:
            show_data(data)
        elif c == 'q':
            break
        else:
            message(". . . ")
            message("Такого пункта нет ")
            sleep(1)
        S("clear")

# ---------------------------[Блок функций BASE-01]----------------------------
PROGRAM_LIST = ["Перевод из одной системы счисления в другую", \
        "Таблица квадратов", \
        "Решение простейшего квадратного уравнения", \
        "Простое искажения текста",\
        "Создание чек-листов"]

def message(msg):
    ''' Выводит анимированное сообщение'''
    for i in range(len(msg)):
        print(msg[:i], end='\r')
        sleep(0.03)
    sleep(0.02)
    print()

def choose_program():
    global PROGRAM_LIST
    choose = ''

    message("Введите номер программы: ")
    for i, item in enumerate(PROGRAM_LIST):
        print(f" ({i+1}) {item}")

    while True:
        choose = input(": ")
        if not choose.isdigit() or int(choose) > len(PROGRAM_LIST):
            message("Вы неверно ввели данные! ")
            continue
        else:
            return int(choose)

def manual():
    global PROGRAM_LIST
    choose = choose_program()

    if choose == 1: print(number_system.__doc__)
    elif choose == 2: print(square_table.__doc__)
    elif choose == 3: print(typical_square.__doc__)
    elif choose == 4: print(psycho.__doc__)
    elif choose == 5: print(check_creator.__doc__)

def program():
    choose = choose_program()

    if choose == 1: number_system()
    elif choose == 2: square_table()
    elif choose == 3: typical_square()
    elif choose == 4: psycho()
    elif choose == 5: check_creator()


# ---------------------------[Главный исполнительный блок]---------------------
message("Привет, " + USER + "! ")
while True:
    ch = input("""
    man -- вызов справки
    Нажать ENTER -- запуск программы
    q -- выход из программы

    """).lower()

    if ch == "man": manual()
    elif ch == "": program()
    elif ch == "q": break
    else: message("Вы неверно ввели данные")

    input("...")
    S("clear")
S("rm -rfv __pycache__")
