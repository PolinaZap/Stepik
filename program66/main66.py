'''
Напишите программу,
на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка,
являющихся крайними,
одним из соседей считается элемент,
находящий на противоположном конце этого списка.

Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''


a = [int(i) for i in input().split()]
lenOfA = len(a) - 1
if len(a) == 1:
    print(a[0])
else:
    i = 0
    while i <= lenOfA:
        if i != lenOfA:
            print(a[i - 1] + a[i + 1], end=' ')
            i += 1
        else:
            print(a[-2] + a[0])
            break
            



