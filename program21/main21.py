'''
требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся фигуры.
'''
from math import sqrt
x = str(input())
if x == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif x == 'круг':
    r = int(input())
    print(3.14 * r ** 2)
elif x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print(sqrt(p * (p - a) * (p - b) * (p - c)))