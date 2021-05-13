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

def dramatic(a):
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
 -- Делает буквы прописными через одну
 -- Убирает знаки препинания
 -- Между слов ставит многоточия
 -- Делает текст капсом и разделяет пробелами буквы
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

def FILE(PATH_FILE, FILE, PATH):
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


