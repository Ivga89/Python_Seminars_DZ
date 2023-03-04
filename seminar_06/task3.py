# Доп задача:
# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, 
# не превосходящее 10^5. Программа должна вывести  все пары дружественных чисел, 
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# n = 1 + a + b + c = m
# m = 1 + a + b + c = n
def dividersFunc(k):
    dividers = []
    for i in range(1, k):
        if k % i == 0:
            dividers.append(i)
    return dividers

def sumOfDividers(dividers):
    sum = 0
    for i in range(0, len(dividers)):
        sum = sum + dividers[i]
    return sum

k = int(input('введите число не превосходящее 1 000 000 (10^5): '))
print(f"Делители числа {k}: ", dividersFunc(k))

for i in range(k + 1):
    # оставлю это здесь, что б не забыть как я пришла к решению
    #print('i = ', i, end = ' ')
    #print('делители: ', dividersFunc(i), end = ' ')
    #print('сумма: ', sumOfDividers(dividersFunc(i)))
    for j in range(k + 1):
        if sumOfDividers(dividersFunc(i)) == j and i == sumOfDividers(dividersFunc(j)) and j != i and i < j:
            print('Дружественные числа: ', i, j)