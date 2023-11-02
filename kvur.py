# import math
# from rumath import koren
from math import sqrt as koren

print('Программа для решения квадратных уравнений!')
bad_data = True

while bad_data == True:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        c = int(input("Введите число c: "))
        bad_data = False
    except ValueError:
        print('Данные не привести к числу')

D = (b * b) - (4 * a * c)
print('Дискриминант равен:', D, '!')

if D > 0:
    d = koren(D)
    X1 = ((-b) + d) / (2 * a)
    X2 = ((-b) - d) / (2 * a)
    print(f'Уравнение имеет 2 корня. X1={X1}, X2={X2}')
elif D == 0:
    X1 = (-b) / (2 * a)
    print('Уравнение имеет 1 корень. X1={}'.format(X1))
else:
    print('Уравнение не имеет корней')
