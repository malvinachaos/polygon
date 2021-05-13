fin = open('in.txt', 'r')
fou = open('ou.txt', 'w')

string = fin.readline()
length = len(string)
fin.close()

for i in range(length - 1):
