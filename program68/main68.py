'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
list = [int(i) for i in input().split()]

lenOfList = len(list)
sortedList = sorted(list)
score = 0

for i in range(0, lenOfList):
    if i == lenOfList - 1:
        if score >= 1:
            print(sortedList[i], end=' ')
        break
    if sortedList[i] == sortedList[i + 1]:
        score += 1
    else:
        if score >= 1:
            print(sortedList[i], end=' ')
            score = 0
