# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите число: '))
result = 0

while n > 0:
    x = n % 10
    result = result + x
    n = n // 10
print(result)