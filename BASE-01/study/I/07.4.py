# на вход подаются три числа. Вывести сначала максимальное, потом
# минимальное, а затем оставшееся
a, b, c = int(input()), int(input()), int(input())

if c <= a >= b:
    print(a)
    if c > b:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif c <= b >= a:
    print(b)
    if a > c:
        print(c)
        print(a)
    else:
        print(a)
        print(c)
elif b <= c >= a:
    print(c)
    if a > b:
        print(b)
        print(a)
    else:
        print(a)
        print(b)
