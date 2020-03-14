# coding=koi8-r
'''
	Функция map принимает функцию и объект-контейнер который может возвращать элементы по одному за раз
	filter фильтрует
'''

listofnums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x * 5, listofnums)))

print(list(filter(lambda x: x % 2 == 0, listofnums)))
