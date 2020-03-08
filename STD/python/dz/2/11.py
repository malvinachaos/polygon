from math import fabs
a,b,c,d = int(input()), int(input()), int(input()), int(input())
FST = fabs(c-a)
SND = fabs(d-b)
if ((FST == 1) and (SND == 2)) or ((FST == 2) and (SND == 1)):
	print("YES")
else:
	print("NO")
