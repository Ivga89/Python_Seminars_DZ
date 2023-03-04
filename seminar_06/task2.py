# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# [-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
# 5
# 15
# Вывод: [1,9,13,14,19]

def indexLookup(min, max, lst, indLst):
    for i in range(len(lst)):
        if lst[i] >= min and lst[i] <= max:
            indLst.append(i)
    return indLst

from random import randint
lst = []
for i in range(randint(10, 20)):
    lst.append(randint(-20, 20))
print(lst)

min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

indexList = []
print(indexLookup(min, max, lst, indexList))
