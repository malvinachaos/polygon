#! /usr/bin/python3

a, blacklist, N, count = [], [], 1, 0

N = int(input('Введите количество чисел: '))

# Блок ввода
for i in range(N):
    a.append(int(input('Введите число: ')))


# Тут сам алгоритм: 
'''
    Нам нужно составить все возможные пары чисел, сумма которых % 7 == 0.
    Проблемы:
        * может произойти такое: a[i] + a[j], где i==j. Такого быть не должно.
        * некоторые пары будут повторяться
'''
for i in range(N):
    for j in range(N):
        # решаем проблему с тем, что мы складывем одно число на себя
        if j != i:
            # решаем проблему с поаторяющимися парами
            if [i, j] not in blacklist and [j, i] not in blacklist:
                if (a[i] + a[j]) % 7 == 0:
                    count += 1
                    blacklist.append([i, j])

print('Количество пар равно: ', count)
