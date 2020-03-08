#! /usr/bin/python3
x = int(input())
while x > 0:
    y = x
    while y > 0:
        y -= 1
        print(y)
    x -= 1
print("Stop")

for x in 1, 5, 2, 4, 3:
    print(x**2)
else:
    print("Done")

'''
    range(start, stop, step)
'''
print(list(range(1, 10, -1)))
print(list(range(1, 10, 1)))
print(list(range(10, 1, -1)))
print(list(range(9, -1, -1)))

