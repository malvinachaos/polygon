name = open("01.исключения.py")
'''
    Открытие файлов:

    variable1 = open("fullname")

    "r" - режим чтения
    "w" - режим записи
    "a" - режим дозаписи(информация будет дописываться в конец файла)
    "b" - бинарный режим(для изображений, музыки и т.д.)
    variable = open("fff", "<r/w/a/b>") -- Можно задать только один режим

    variable.close() #Закрытие файла
'''
name.close()
#чтение данных из файла:
a = open("txt.txt", "r")
cont = a.read()
print("Длина файла --", len(cont),"символов")
print(cont)
a.close()

#прочитать определëнное количество байт
a = open("txt.txt", "r")
print(a.read(3)) #Прочитать первые 3 байта. Получается, курсор смещается на 3 позиции вправо
print(a.read(4)) #Прочитать следующие 6 байт. Курсор смещается на 6 позиций вправо
print(a.read(-5)) #Передвинуть курсор на пять позиций вправо. Стереть 5 символов
print(a.read()) #Прочитать оставшиеся байты`
a.close()

print("\n -----------------------------------------------\n\n")
print("Чтение данных их файлов построчно, выводя КАЖДЫЙ символ")
megafile = open("two.txt", "r")
print(megafile.readlines())
megafile.close()
print("\n**************************************************\n")
megafile = open("two.txt", "r")
for line in megafile:
    print(line)

megafile.close()
print(len(open("two.txt").readlines()))

print("\n**************************************************")
print("**************************************************\nЗапись в файл\n")

Arch = open("btw.txt", "w")
#Запись
Arch.write("btw, i use arch")
print("Info about file:\n", Arch)
print("Count of symbols:",Arch.write("btw, i use arch"))
Arch.close()

#Чтение
Arch = open("btw.txt", "r")
print(Arch.read())
Arch.close()

print("\n**************************************************")
print("**************************************************\nРаботаем с файлами\n")
'''
    Для точной уверенности, что файл будет закрыт, даже если произойдёт ошибка,
    стоит использовать конструкцию try/finally
'''
try:
    F = open("01.исключения.py", "r")
    print(F.read())
finally:
    F.close()
print("\n-------Конструция with/as-------")
with open("02.техника_призыва_исключения.py") as f:
    print(f.read())
print("Файл автоматически закрылся")

