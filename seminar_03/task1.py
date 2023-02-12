# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
randomList = list()
for i in range(0, 10):
    randomList.append(randint(1, 10))
    
print(randomList)
n = int(input('Введите число от 0 до 10 для поиска в массиве: '))
count = 0
for i in range(len(randomList)):
    if randomList[i] == n:
        count += 1
print('число ' + str(n) + ' встречается в массиве ' + str(count) + ' раз(а)')
