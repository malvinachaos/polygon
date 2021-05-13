# подсчитывать слова, разделённые пробелом и выводить получившуюся статистику
words = input().lower().split()
sense = set(words)

for i in sense:
    print(i, words.count(i))
