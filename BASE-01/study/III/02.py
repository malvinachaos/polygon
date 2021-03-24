def modify_list(l):
    i = 0
    length = len(l)
    while i < length:
        if l[i] % 2 != 0:
            l.pop(i)
            length -= 1
        else:
            l[i] //= 2
            i += 1

ls = [int(i) for i in input().split()]
modify_list(ls)
print(*ls)
