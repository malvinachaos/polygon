from math import fabs
a,b,c,d = int(input()), int(input()), int(input()), int(input())
if (fabs(d-b) == fabs(c-a)) or (a == c or b == d):
    print("YES")
else:
    print("NO")
