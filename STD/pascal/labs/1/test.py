#! /usr/bin/python3
from os import system as S


with open("TEST", 'r') as T:
    tmp = open("tmp_test", "w")
    tmp.write(T.readline())
    tmp.close()
    command = "./half-circle_n_square < tmp_test"
    S(command)
    S("rm tmp_test")
