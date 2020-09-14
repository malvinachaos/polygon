#! /usr/bin/python3
from random import randint as r

with open("TEST", "w") as T:
    n = int(input("Введите колво тестов: "))
    T.write(str(n) + "\n")
    for i in range(n):
        a = str(r(-10, 10)) + " " + str(r(1, 10)) + " " + str(r(-10, 10)) + " " + str(r(1, 10)) + " " + str(r(1, 3))
        fail = str(r(-10, 10)) + " " + str(r(-9, 0)) + " " + str(r(-10, 10)) + " " + str(r(0, 1)) + " " + str(r(-3, 3))
        if i % 4 == 0:
            T.write(fail + "\n")
        else:
            T.write(a + "\n")
