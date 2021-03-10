#! /usr/bin/python3
from os import getcwd, getlogin, mkdir, listdir
from os import system as S
from os.path import abspath, isdir, join
from time import sleep
from colored import fg, bg, attr
import math_core
import psycho
import check_creator


# установка

if not isdir(".base_01_files"):
    mkdir(".base_01_files")

PATH = getcwd()
USER = getlogin()
FILE = "/.base_01_files"
PATH_FILE = listdir(PATH+FILE)

S("clear||cls")

# Титульный экран
print("\n\tBASE-01 v0.3.0\n\n\tMADE BY LAZY DRAGON!\n\n\n\
Создан 29.03.2020\nПоследнее обновление 03.03.2021")

sleep(2)
S("clear||cls")



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

    if choose == 1: print(math_core.number_system.__doc__)
    elif choose == 2: print(math_core.square_table.__doc__)
    elif choose == 3: print(math_core.typical_square.__doc__)
    elif choose == 4: print("Искажает текст")
    elif choose == 5: print("Создаёт и искажает чек-листы")

def program():
    choose = choose_program()

    if choose == 1:
        number, base = input("Введите число: ").upper(), \
					int(input("Введите его основание: "))
        new_base = int(input("Введите систему счисления: "))
        
        print("Решение задачи:", math_core.number_system(number, base, new_base))
    elif choose == 2: math_core.square_table()
    elif choose == 3: math_core.typical_square()
    elif choose == 4:
        ch = ''
        while True:
            print("""
 (f) -- Редактирование из файла
 (k) -- Редактирование с клавиатуры
 (q) -- Выход
        """)
            ch = input(": ")

            if ch.lower() == 'f': psycho.FILE()
            elif ch.lower() == 'k': psycho.KEYBOARD()
            elif ch.lower() == 'q': break

    elif choose == 5:
        CHECKLIST = ''
        psycho.make_check_list(CHECKLIST, PATH_FILE)
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
                psycho.write_data(data, CHECKLIST)
            elif c == 'e':
                data = psycho.edit_data(data)
            elif c == 's' and data != []:
                psycho.show_data(data)
            elif c == 'q':
                break
            else:
                message(". . . ")
                message("Такого пункта нет ")
                sleep(1)
            S("clear||cls")



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
    S("clear||cls")
