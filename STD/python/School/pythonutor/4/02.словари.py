'''
    Словари это структура данных, которые используются для хранения производьных
    ключей, и заданн их значениями
    words = {} -- пустой словарь 
'''
accounts ={"root": 0, "marina": 25345, "alisa": 86445}
print(accounts)
print(accounts["marina"])
'''
    Словарь нельзя изменить
    code = {[1,2,3]: "one, two, three"} -- вызовет ошибку TypeError
    <имя словаря> = {<ключ>:<значение>}
    (!) Обратиться можно к ключу, а не к значению ключа
'''
del accounts
word = {0:"false", 1:"true", 42:"Truth", 86:47,47:86}
word[9] = 86
print(word[word[9]])
print("True" not in word)
print(42 in word)

# словарь.get() -- возвращает значение ключа
print(word.get(42))
print(word.get(292929))
print(word.get(982, "Aaaaa\n"))

print(word.get(86) + word[word[47]], "\n")

