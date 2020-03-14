#Можно использовать контрукцию try exept, чтобы обойти ошибку
try:
    #Здесь находится код, который модет вызвать ошибку
    print(0/0)
    print("3"/3)
except ZeroDivisionError:
    print("0 was a mistake\n")
except (ValueError, TypeError):
    print("Type is wrong, value is a mistake\n\n")
'''
Частые ошибки
    ImportError: импортирование не удалось; 
    IndexError: индекс не входит в диапазон элементов списка; 
    NameError: попытка использовать несуществующую переменную;
    SyntaxError: ошибка разбора кода; 
    TypeError: в функцию передано значение несовместимого типа; 
    ValueError: в функцию передано значение совместимого типа, 
    но с некорректным значением.

'''
try:
    d = 43/0
    f = "d"/3
    import SUUUU
except:
    print("Ыы, я перехватила все ошибки\n")

try:
    d = int(input())
    s = 42/d
except ZeroDivisionError:
    print("Ыыы, ашибачка")
finally:
    print("\nЭтот код будет раьотать в любом случае, кст знач. d =", s)

'''
    В except можно вызвать raise, тогда ошибка повторно будет вызвана
'''

try:
    num = 2/0
except:
    print("zero")
    raise 
