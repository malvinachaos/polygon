Dat = [7, 9, 10, 5, 6, 7, 9, 8, 6, 9]
m = 10
n = 0
for k in range(0,10):
    if Dat[k] < m:
        m = Dat[k]
        n = k + 1
print (n)
