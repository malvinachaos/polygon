from colored import fg, bg, attr


def number_system(m, n, new_ns):
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

    return dec_to_ns(n_to_dec(m, n, NUM), new_ns, NUM)

def square_table():
    ''' Рисует таблицу квадратов от 10 до 99
    '''
    # Цвета G -- зелёный, B -- синий, C -- голубой, reset -- сброс цвета
    G , B, C, reset = \
					fg("#000000") + bg("#00FA9A"), \
					fg("#000000") + bg("#4169E1"), \
					fg("#000000") + bg("#00BFFF"), \
					fg("#ffffff") + bg("#000000")

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
        print("это уже не квадратное уравнение\n\n")
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

