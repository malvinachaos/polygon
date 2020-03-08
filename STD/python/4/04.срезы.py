# Интересный способ получения значений из списка
n = 0
spisok = []
for n in range(10):
    spisok.append(n) 
print(spisok)

print(spisok[2:7])
print(spisok[2:3], "\n")

print(spisok[:3])
print(spisok[3:])

#Задаём шаг

print(spisok[::2], "\n") # Выводим чётные числа

#Получение среза с конца
print(spisok[1:-1])

print(spisok[::-1], "\n\n")
del spisok
#Быстрое создание списка
squares = [i**2 for i in range(10)]
print(squares, "\n"+ "---------"+ "\n")
spisok = [i+1 for i in range(10)]
print(spisok, "\n" + "---------" +"\n")
#Этот метод взят из математики, а именно из нотации построения множества
squares = [i**2 for i in range(10) if i**2 % 2 == 0]
print(squares, "\n"+ "---------"+ "\n")
#Попытка создания очень обширный список приведёт к MemoryError

