# coding=koi8-r

'''
	Чёт я не помнимаю эти генераторы
'''

def countown():
	i = 5
	while i >= 0:
		yield i
		i -=1

for i in countown():
	print(i)

