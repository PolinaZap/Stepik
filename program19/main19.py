'''
Напишите программу, принимающую на вход целое число,
которая выводит True,
если переданное значение попадает в интервал
(−15,12]∪(14,17)∪[19,+∞)
и False в противном случае
'''
x = int(input())

if x > - 15 and x <= 12:
    print('True')
elif x > 14 and x < 17:
    print('True')
elif x >= 19:
    print('True')
else:
    print('False')