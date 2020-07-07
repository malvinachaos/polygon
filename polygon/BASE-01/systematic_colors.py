#! /usr/bin/python3

from os import popen, system as S
from colored import bg, attr
from time import sleep

# setting window's size
a = popen("stty size", "r").read().split()
HEIGHT, WIDTH = int(a[0]), int(a[1])
del a

def circle(x, y, a, b, r):
    return ((x - a)**2)*2 + ((y - b)**2)//2 <= r**2

def square(x, y, a0, a1, b0, b1):
    return a0 <= x <= a1 and b0 <= y <= b1

def parabola(x, y):
    return y >= x**2

# colors
base = " " + attr(0)
C0 = bg("#231290") + base
C1 = bg("#00F125") + base
C2 = bg("#451105") + base
C3 = bg("#ab9011") + base
C4 = bg("#ff6511") + base

# drawing background
for i in range(HEIGHT):
    for j in range(WIDTH):
        if parabola(HEIGHT - i, j):
            print(C4, end='')
        elif circle(i, j, 10, 195, 55):
            print(C3, end='')
        elif circle(i, j, 50, 60, 35):
            print(C1, end='')
        elif square(i, j, 20, 90, 0, 90):
            print(C2, end='')
        else:
            print(C0, end='')
input()
