# Для сна нужно x минут
# Ложится спать после полуночи в h часов, m минут
x, h, m = int(input()), int(input()), int(input())
x += (h*60+m)
print((x//60)%24, x%60, sep="\n")
