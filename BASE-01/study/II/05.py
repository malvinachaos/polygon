# считывает a, b
# выволит среднее арифметическое всех чисел их отрезка [a,b], кратные трём.

a, b = int(input()), int(input())
middle = 0
count = 0

for i in range(a, b+1):
    if i % 3 == 0:
        middle += i
        count += 1

print(middle/count)