# coding=koi8-r
'''
	Лямбда-функции могут делать так, как представлено снизу
'''

def mydd(f, arg):
	return f(arg)

print(mydd(lambda x: 2*x*x, 5)) # Также это называется анонимной функцией. Анонимная, потому что нет имени
del mydd

def usr(hello, name):
	print hello(name)

usr(lambda e: "Hello, " + e, "Marina")

print("\n--Лямбда-функции ограничены только 1 строкой, когда как именованные имеют неогран-е кол-в строк--\n")

# Также можно присваивать переменным
thing = lambda x, z: x**3//z
print(thing(7, 80))
