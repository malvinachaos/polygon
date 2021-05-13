# написать вывод таблицы умножения
# принимаются a, b, c, d
# программа должна вывести фрагмент таблицы умножения для всез чисео [a,b] на все числа [c,d]
# {a, b, c, d} c Nm a <= b и c <= d

a, b = int(input()), int(input())
c, d = int(input()), int(input())

for i in range(c, d+1):
    print('\t', i, sep='', end='')
print()

for i in range(a, b+1):
    print(i, '\t', sep='', end='')
    for j in range(c, d+1):
        print(i*j, '\t', sep='', end='')
    print()
