#Требуется определить, является ли данный год високосным.
x = int(input('Введите числовое обозначение года:'))
if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
    print('Это обычный год!')
else:
    print('Это високосный год!')