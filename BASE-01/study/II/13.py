# Считывает список чисел lst из первой строки
# и x из второй, выводящая все позиции, на которых встречается число x
# в переданном списке lst
lst = [int(i) for i in input().split()]
x = int(input())
flg = True

for i, item in enumerate(lst):
    if item == x:
        print(i, end=" ")
        flg = False

if flg:
    print("Отсутствует")
else:
    print()

'''
ЛУЧШЕЕ РЕШЕНИЕ
l = [int(i) for i in input().split()]
x = int(input())

if not x in l:
    print("Отсутствует")
for i, item in enumerate(l):
    if item == x:
        print(i, end=" ")
'''
