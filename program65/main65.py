'''
Напишите программу,
на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.

Используйте метод split строки.
'''
a = [int(i) for i in input().split()]
print(sum(a))

a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
print(s)

