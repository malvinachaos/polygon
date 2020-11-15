#! /usr/bin/python3
from colored import fg, bg, attr
from os import get_terminal_size
import argparse


C1 = bg("#875faf")
R  = attr("reset")
C2 = bg("#5f5fd7") + fg("#87afaf")

# File
parser = argparse.ArgumentParser(prog="Drawing ascii",\
                                 description="Coloring ascii text",)

parser.add_argument("file", metavar = "file.txt", type=argparse.FileType("r"),\
                    help="simple ascii drawing")

parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1")

arg = parser.parse_args()

for i in arg.file.read():
    if i != " ":
        print(C2+i+R, end="")
    elif i == " ":
        #print(C1+i+R, end="")
        print(i, end="")
    else:
        print(i, end="")
