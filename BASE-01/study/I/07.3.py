choose = input()

if choose == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**(0.5))
elif choose == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a*b)
elif choose == 'круг':
    r = int(input())
    print(3.14*r**2)
