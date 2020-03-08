#Объявление функции 'print_you'
def print_you():
    print("I print you")

#Вызов функции

print_you()

#Функция с параметрами
def func_par(x, y):
    if (x > y):
        print("XX")
    else:
        print("XY")

print("\nРабота функции с параметрами")
x = int(input("Введите цел. число для x"))
y = int(input("Введите цел. число для y"))
func_par(x, y)

del x
del y

print("Работа функции, выполняющая некие арифм. операции")
def sumnot(x, y):
    return (x+y/(x-x+y**2))

summon = sumnot(2, 5)
print(summon)
'''
 Это строки документации

 Алаллаалалла
'''
#Также можно назначить переменной функцию
megasummon = sumnot
def xx(func, s):
    t = func * s
    print("Ssssssss ", t)

xx(megasummon(4, 78), 56)
