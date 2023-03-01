# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degreeRec(number, degree):
    if degree == 0:
        return 1
    return number * degreeRec(number, degree - 1)

number = int(input('Enter number: '))
degree = int(input('Enter degree: '))

print(degreeRec(number, degree))