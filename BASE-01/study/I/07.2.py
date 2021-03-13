# 1е, 2е число и операция.
# операция: +, -, /, *, mod, pow, div
# Если деление на ноль, то вывести 'Деление на 0!'

a, b, op = float(input()), float(input()), input()

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '/':
    if b != 0:
        print(a/b)
    else:
        print('Деление на 0!')
elif op == '*':
    print(a*b)
elif op == 'mod':
    if b != 0:
        print(a%b)
    else:
        print('Деление на 0!')
elif op == 'div':
    if b != 0:
        print(a//b)
    else:
        print('Деление на 0!')
elif op == 'pow':
    print(a**b)
