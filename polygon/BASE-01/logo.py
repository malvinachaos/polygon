#! /usr/bin/python3
from colored import fg, bg, attr
from os import system as S
from os import popen

# screen size
a = popen("stty size", "r").read().split()
HEIGHT, WIDTH = int(a[0]), int(a[1])
del a

# colors
C0 = bg('#af00ff') + "  " + attr(0)
C1 = bg('#8700af') + "  " + attr(0)
C2 = bg('#d700d7') + "  " + attr(0)
C3 = bg('#d787af') + "  " + attr(0)
C4 = bg('#dfa7df') + "  " + attr(0)


# Logo. 33x12
BASE_LOGO = [\
        C2*33,\
        C2 + C0*6 + C2*4 + C0*3 + C2*4 + C0*6 + C2*2 + C0*6 + C2,\
        C2 + C0*2 + C1*2 + C0*3 + C2*2 + C0*2 + C1 + C0*2 + C2*2 + C0*6 + C2*2 + C0*6 + C2*2,\
        C3*2 + C0*2 + C1*2 + C0*2 + C3 + C0*2 + C1*3 + C0*2 + C3 + C0*2 + C3*6 + C0*2 + C3*6,\
        C3*2 + C0 + C1*2 + C0*3 + C3 + C0 + C1*2 + C0 + C1*2 + C0 + C3 + C0*5 + C3*3 + C0*2 + C3*6,\
        C4*2 + C0*5 + C4*2 + C0 + C1 + C0*3 + C1 + C0 + C4*2 + C0*5 + C4*3 + C0*6 + C4,\
        C4*2 + C0*5 + C4*2 + C0*7 + C4*5 + C0*3 + C4*2 + C0*6 + C4,\
        C3*2 + C0 + C1*2 + C0*3 + C3 + C0*3 + C3 + C0*3 + C3*6 + C0*2 + C3 + C0*2 + C3*6,\
        C3*2 + C0*2 + C1*2 + C0*2 + C3 + C0*3 + C3 + C0*3 + C3*5 + C0*3 + C3 + C0*2 + C3*6,\
        C2 + C0*2 + C1*2 + C0*3 + C2 + C0*2 + C2*3 + C0*2 + C2*2 + C0*6 + C2 + C0*6 + C2*2,\
        C2 + C0*6 + C2*2 + C0 + C2*5 + C0 + C2 + C0*6 + C2*3 + C0*6 + C2,\
        C2*33\
        ]

# Background. 6x12

BASE_LOGO_MIDDLE = [C2, C2, C2, C3, C3, C4, C4, C3, C3, C2, C2, C2]

W = (WIDTH//2 - 33)//2
H = HEIGHT//2 - 6

S("clear")
for i in range(H+1):
    print('\n' + BASE_LOGO_MIDDLE[0]*(2*W + 33), end='')

for i, item in enumerate(BASE_LOGO):
    print('\n' + BASE_LOGO_MIDDLE[i]*W + item + BASE_LOGO_MIDDLE[i]*W,  end='')

for i in range(H):
    print('\n' + BASE_LOGO_MIDDLE[0]*(2*W + 33), end='')
input()
