# key, value -- числа
# если key есть, то добавить value в список, который хранится по этому ключу
# если его нет, то нужно добавить значение в список по ключу 2*key
# если и его нет, то нужно его добавить и сопсотавить ему список из переданного
# элемента [value]
''' ЛУЧШЕЕ РЕШЕНИЕ(ГСПДИ, Я НЕ ПОНИМАЮ, КАК):
# True -> 1
# False -> 0
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]

'''
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif key not in d.keys():
        if 2*key in d.keys():
            d[2*key].append(value)
        else:
            d.update({2*key: [value]})


joke = dict()
update_dictionary(joke, 1, -1)
print(joke)
update_dictionary(joke, 2, 3)
print(joke)
update_dictionary(joke, 3, 4)
print(joke)
update_dictionary(joke, 3, 8)
print(joke)
