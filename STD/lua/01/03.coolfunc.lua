-- dofile() открывает и выполняет файл
dofile("01.lua")
dofile("02.typedata.lua")

-- tonumber() преобразует переменную в число
-- tostring() обратно
a = "345"
print(type(a), '-', a)
a = tonumber(a)
print(type(a), '-', a-1)
a = tostring(a)
print(type(a), '-', a)
b = 'F'
print(b)
print(type(b))
b = tonumber(b)
print(b)
print(type(b))
print("Если строка состоит из чисел, то луа конвертирует в int, в противном случае получится nil")
-- _VERSION глобальная переменная, возвращает версию lua
-- rawequal
if rawequal(1,1) == true then
	a = "SSS"
end

if a == "SSS" then
	print(1)
end

a,b,c = 1,"SUDO RM",3
print(a, ' ', b, ' ', c)

local a2 = a; -- переменная a на какое-то время имеет значение a2

