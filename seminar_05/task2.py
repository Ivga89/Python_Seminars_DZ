# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.

# 2 2
# 4

def sum(a, b):
    if b == 0:
        return 0
    return a + sum(a, b - 1)

a = int(input('Enter a: '))
b = int(input('Enter b: '))

print(sum(a, b))