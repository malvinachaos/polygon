# На вход в программу подаётся прямоугольная матрица в виде последовательности строк
# Терминальное слово -- end

# Выводит матрицу того же размера, у которой каждый элемент i,j == сумме 
# элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1)

lst = []
while True:
    num = input()
    if num == "end":
        break
    else:
        lst.append([int(i) for i in num.split()])

size = len(lst)
for i in range(size):
    two_size = len(lst[i])
    for j in range(two_size):
        k, l = 0, 0
        if i < size-1: k = i+1
        if j < two_size-1: l = j+1
        print(lst[i][j-1] + lst[i-1][j] + lst[k][j] + lst[i][l], end=" ")
    print()

'''
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
'''
