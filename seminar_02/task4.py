# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

from random import randint

n = randint(2, 20)
print(n, end = ": ")
for i in range(n + 1):
    if i * i < n:
        print(i, end = ' ')