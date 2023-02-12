# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
x = int(input('Введите число X от 0 до 10: '))
n = int(input('Введите количество элементов в массиве: '))
randomList = []
minList = []
for i in range(0, n):
    randomList.append(randint(1, 9))
    minList.append(abs(x - randomList[i]))
print(randomList)

min = 10
for i in range(0, n):
    if minList[i] < min and minList[i] != 0:
        min = minList[i]
        index = i
print('Самый близкий по величине элемент к заданному числу X (' + str(x) + ') = ' + str(randomList[index]))