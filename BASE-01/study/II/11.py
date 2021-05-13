# считываем числа до тех пор, пока их сумма не будет равна нулю
# при этом, мы должны сразу вывести сумму квадратов 
a = []

while True:
    a.append(int(input()))
    if sum(a) == 0:
        break
print(sum([i**2 for i in a]))
'''
ЛУЧШЕЕ РЕШЕНИЕ
s = [int(input())]
while sum(s) != 0:
    s.append(int(input()))

print(sum([i**2 for i in s]))
'''
