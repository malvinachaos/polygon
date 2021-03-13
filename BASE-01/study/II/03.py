# Если число меньше 10, пропускаем его
# Если число больше 100, то прекращаем считывать числа
# в остальных случаях вывести это число обратно на консоль в отдельной строке

result = ''
while True:
    c = int(input())
    if c < 10:
        continue
    if c > 100:
        break
    else:
        result += str(c)+'\n'

print(result, end='')
'''
ГЕНИАЛЬНОЕ РЕШЕНИЕ
x = 0
while x <= 100:
    if x > 9:
        print(x)
    x = int(input())
'''