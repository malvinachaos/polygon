from colored import fg, bg, attr
B0 = bg('#262626') + "  " + attr(0)
C0 = bg('#af00ff') + "  " + attr(0)
C1 = bg('#8700af') + "  " + attr(0)
C2 = bg('#d700d7') + "  " + attr(0)
C3 = bg('#d787af') + "  " + attr(0)
C4 = bg('#dfa7df') + "  " + attr(0)

SQUARE = (B0*32+'\n') * 32

x, y = 0, 0

for i in range(32):
    for j in range(32):
        if i >= j**2:
            SQUARE[i*j] = C0

print(C0)
