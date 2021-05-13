# Минимум часов сна -- A, максимум -- B
# Аня спит H часов
a, b, h = int(input()), int(input()), int(input())

if a <= h <= b:
    print("Это нормально")
elif h < a:
    print("Недосып")
else:
    print("Пересып")
