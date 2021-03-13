# Написать программу, вычисляющая процентное содержание символов G и C
count = 0
code = input().lower()

for i in code:
    if (i == 'g') or (i == 'c'):
        count += 1

print(count/len(code) * 100)
'''
ЛУЧШЕЕ РЕШЕНИЕ
code = input().lower()
print((code.count('g') + code.count('c'))/len(code) * 100)
'''