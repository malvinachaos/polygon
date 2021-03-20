# Создаём поле
row, col, count_mines = (int(i) for i in input().split())
field = [[0 for j in range(col)] for i in range(row)]

# Вводим координаты мин
for i in range(count_mines):
    m, n = (int(i) - 1 for i in input().split())
    field[m][n] = -1

for i in range(row):
    for j in range(col):
        if field[i][j] == 0:
            for l in range(-1, 2):
                for k in range(-1, 2):
                    a = i + l
                    b = j + k

                    if (0 <= a < row) and (0 <= b < col) and (field[a][b] == -1):
                        field[i][j] += 1

for i in range(row):
    for j in range(col):
        if field[i][j] == -1:
            print('*', end=' ')
        elif field[i][j] == 0:
            print('.', end=' ')
        else:
            print(field[i][j], end=' ')
    print()
