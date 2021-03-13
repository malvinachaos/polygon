num = sorted([int(i) for i in input().split()])
nums = []

# перемещение по списку, 
for i in num:
    if (num.count(i) > 1) and (i not in nums):
        nums.append(i)
        print(i, end=' ')
'''
Топовое решение
ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
'''