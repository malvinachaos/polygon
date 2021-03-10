import pickle


def make_check_list(ch, PATH_FILE):
    ch =  [x for x in PATH_FILE if ".data" in x]


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
            S("clear||cls")
            continue
        else: c = int(c)

        if c > len(CHECKLIST)-1:
            message("Вы неверно ввели даные!!")
            sleep(1)
            S("clear||cls")
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
        S("clear||cls")
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

