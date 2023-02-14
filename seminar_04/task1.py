# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
lst1 = list()
lst2 = list()
for i in range(0, n):
    lst1.append(int(input()))
for i in range(0, m):
    lst2.append(int(input()))
set1 = set(lst1)
set2 = set(lst2)
inters = list(set1.intersection(set2))
interList = list()

for i in range(len(inters)):
    pos = i
    for j in range(i + 1, len(inters)):
        if inters[j] < i:
            pos = j
        temp = inters[i]
        inters[i] = inters[pos]
        inters[pos] = temp
#interList.append(i)

print('Первый набор чисел: ', lst1)
print('Второй набор чисел: ', lst2)
print('Числа встречающиеся в обоих множествах в порядке возрастания: ', inters)