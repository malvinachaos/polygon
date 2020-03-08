#! /usr/bin/python3
# coding=koi8-r
'''
	Списано с учебника
	если шо, вот ввод ./sum2.py < in.txt
'''

print("Type ints, each followed by Enter: or ^D or ^Z to finish")

total = 0
count = 0

while True:
	try:
		line = input()
		if line:
			number = int(line)
			total += number
			count += 1
	except ValueError as err:
		print(err)
		continue
	except EOFError:
		break

if count:
	print("count =", count, "total =", total, "mean =", total/count)
