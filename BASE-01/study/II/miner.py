# Создаём поле
row, col, count_mines = (int(i) for i in input().split())
field = [[0 for j in range(col)] for i in range(row)]

# Вводим координаты мин
for i in range(count_mines):
    m, n = (int(i) for i in input().split())
    field[m][n] = -1

for i in range(row):
    for j in range(col):
        if field[i][j] == 0:
