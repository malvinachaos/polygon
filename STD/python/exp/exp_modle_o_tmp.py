#! /usr/bin/python3
# coding=utf-8

# ⚧ = "unicod, motherfucker!" Так нельзя, увы
# m = '⚧' А так можно
'''
	#### Некий вывод ####
>>> five = 5
>>> two = 2
>>> five and two
2
>>> two and five
5
>>> bool(two) and bool(five)
True
>>> bool(None)
False


'''


x = ['Madara']
y = []
x.append('Uchiha')
list.append(y, 'Obito')
list.append(y, x[1])
print(x[0], 'and', y[0], y[1]+'s')

# Оператор 'is' -- оператор идентичности
'''
	Этот оператор сравнивает только адреса памяти, в которых располагаются
	объекты, а не сами объекты

	#### Продолжение ####
>>> m is '⚧'
False
>>> '⚧' is '⚧'
True
>>> x = m
>>> x
'⚧'
>>> m
'⚧'
>>> x is m
True

'''
print(4 is 4)
print(4 is 0)
print(1 is True)
print(bool(0) is False)
print(bool(42) is True, "\n\n")
del x, y
x = 5
y = 5
print(x is not None)

print(0 <= x <= 5)
'''
	Оператор членства 'in' --- ищет данный объект в списке/кортеже/словаре/строк
	е
'''

x = [1, 2, 3, 4, 5, 6 ]
print("\n\n#############################################")
print(5 in x)
print("List \'x\' has 7:", 7 in x)
print("List \'x\' has 3:", 3 in x)
print('Some word in frase:' ,'fuck' in 'So, NVIDIA, fuck you')

print('\n\n#############################################\n')
if x[4] == int(input("Введи 5 или любое число ")): # 5 или любое значение
	print('Does')
	# Работает. Главное, чтобы были отступы

	print('It works?')


	print('Realy?')

for k in x:
	print(x[k-1], 'or', k)

print('\n\n#############################################\n')
for l in "абвгдеёжзийклменопрстуфхцчшщъыьэюя":
	if l in "пидор":
		print(l)
print('На самом деле здесь должно быть слово \'пидор\'')

s = input("Введи число 3.5: ")
try:
	i = int(s)
	print('valid integer entered:', i)
except ValueError as err:
	print('Оказывается и так можно. Мощная штука, эта \'as\';', err)

'''
	Немного об операторах

>>> spam = ['eggs']
>>> spam
['eggs']
>>> spam += 'spam'
>>> spam
['eggs', 's', 'p', 'a', 'm']
>>> spam -= 'spam'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -=: 'list' and 'str'
>>> spam += "spam"
>>> spam
['eggs', 's', 'p', 'a', 'm', 's', 'p', 'a', 'm']
>>> spam += ['spam']
>>> spam
['eggs', 's', 'p', 'a', 'm', 's', 'p', 'a', 'm', 'spam']
>>> spam += [42]
>>> spam
['eggs', 's', 'p', 'a', 'm', 's', 'p', 'a', 'm', 'spam', 42]
'''
print('\n\n#############################################\n')

msg = 'Input integer character '
def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)

i = get_int(msg)
print('Вот вам и', i)

'''
    Немного о числах

>>> s = int(input('Input: '))
Input: 3.2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.2'
>>> s = int(input('Input: '))
Input: 10//3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '10//3'
>>> s = int(10/9)
>>> s
1
>>> s = int(input('Input: '))
Input: 9/5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9/5'
>>> 9/5
1.8
>>> s = int(input('Input: '))
Input: 9//9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9//9'
>>> del s
>>> s = input(int())
06
>>> s
'6'
>>> s = int(input(int()))
09//9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9//9'
>>> s = int(9//9)
>>> s
1

'''

print('\n\n#############################################\n')
'''
        ### Поговорим о модулях ###
    Модули -- это обычные файлы с расширением *.py, содержащий в себе
    функции и классы

    import sys
'''
'''
import example.py
some_int = int(input("Input int chatacter:: "))
some_int = example.inverse(some_int)
print('Это работает, наверное...', some_int)
Этот код не работает. Разберись, почему
'''
from random import choice as chse
s = chse(["Linux", "Windows", "macos"])
print(s)



