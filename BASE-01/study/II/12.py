n, i = int(input()), 0

if n > 2:
    for j in range(n):
        for k in range(j):
            if i < n:
                print(j, end=" ")
            i += 1
elif n == 1:
    print(1)
elif n == 2:
    print('1 2 ')

print()
