#! /usr/bin/python3
from os import system as S


with open("TEST", 'r') as T:
    n = int(T.readline()[:-1])
    for i in range(n):
        S("clear")

        print(f"Test №{i+1}", end="\n\n")
        tmp = open("tmp_test", "w+")
        tmp.write(T.readline()[:-1])
        tmp.seek(0)
        txt = tmp.read().split()
        print(f"{txt[0]} {txt[1]}\n{txt[2]} {txt[3]}\n{txt[4]}", end="\n\n")
        tmp.close()

        command = "./half-circle_n_square < tmp_test"
        S(command)
        input("\n\nENTER...")
        S("rm tmp_test")
