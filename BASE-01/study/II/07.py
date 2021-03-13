# aaaabccbb -> a4b1c2b2
# Не хватает итераций

code = input()
compress = code[0]
count = 1
i = 0
j = 0
n = len(code)

for i in range(1, n):
    if compress[j] == code[i]:
        count += 1
        # print(f'yes, {count} | {code[i]}', end='\t')
    else:      
        compress += str(count) + code[i]
        j += len(str(count)) + 1
        count = 1
        # print(f' no, j is {j} | count is {count} | new symbol is {compress[j]} | {code[i]}', end='\t')
    # print()
compress += str(count)

print(compress)
'''
ТОПОВОЕ РЕШЕНИЕ

genome = input() + ' '
s = 0
n = genome[0]
for i in genome:
    if n != i:
        print(n + str(s), end = '')
        s = 0
        n = i
    s += 1
'''