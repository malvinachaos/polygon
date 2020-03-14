b1 = int(input())
b2 = int(input())
w1 = int(input())
w2 = int(input())
#Проверка на чётность рядов
if ((b1%2!=0) and (w1%2!=0) or (b1%2==0) and (w1%2==0)):
    if((b2%2!=0) and (w2%2!=0) or (b2%2==0) and (w2%2==0)):
        print("YES")
    else:
        print("NO")
else:
    if((b2%2!=0) and (w2%2==0) or (b2%2==0) and (w2%2!=0)):
        print("YES")
    else:
        print("NO")
'''
    Ответ:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
'''
