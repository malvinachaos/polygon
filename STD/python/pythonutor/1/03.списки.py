Command = ['PATA', "PON", "DON", "CHAKA"]
print("Работа оператора \'in\'\n")
print("Дан массив Command, состояий из 5 элементов:\n ", Command)

print("PON есть в массиве -- ","PON" in Command)
print("DODON есть в массиве -- ","DODON" in Command)

print("not также можно использовать с in")

print("\nРабота функции append:\n")

print(Command+ " до\n")
Command.append("DODON")
print(Command+ "после\n")

print("Радота функции len:\n")
print("В массиве " + str(len(Command)) + " элементов\n")

print("Работа функции insert:\n")

print(Command, " до\n")
Command.insert(1, "PATA")
print(Command, " после\n")

print("Работа функции index:\n")

print("Индекс элемента \'PON\' ", Command.index("PON"))
print("Индекс элемента \'PATA\' ", Command.index("PATA"))
