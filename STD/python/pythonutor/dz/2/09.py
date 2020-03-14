from math import fabs
a,b,c,d = int(input()), int(input()), int(input()), int(input())
if fabs(d-b) == fabs(c-a):
    print("YES")
else:
    print("NO")
