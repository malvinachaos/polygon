# считывает строку с числом n, задающее количество чисел, которые нужно считать
# далле считывает n чисел. Должно в итоге получиться n+1 строк
# При считывании x_i программа должна на отдельной строке вывести значение f(x_i)
# def f(x) уже реализована. Она вычисляется достаточно долго, поэтому надо избежать пов
# торного вычисления значений
def f(x):
    return x + 500

n = int(input())
table = dict()
final = list()

for i in range(n):
    j = int(input())
    if j not in table.keys():
        table.update({j: f(j)})
    final.append(table[j])

print(*final, sep='\n')
''' ЛУЧШЕЕ РЕШЕНИЕ, ЭТО ПРОСТО ГЕНИАЛЬНО
a = [int(input()) for i in range(int(input()))]
b = {x:f(x) for x in set(a)}
for i in a:
    print(b[i])

'''
