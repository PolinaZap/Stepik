x = int(input('Сколько равно 2 + 2? Введите ответ:'))
score = 0


if x == 4:
    print('Верно! Вы заработали 1/1 баллов.')

    score += 1

elif x < 4:
    print('Неверно! Ваш счет - 0.')
    print('У Вас есть вторая попытка! ')
    y = int(input('Сколько равно 50/25? Введите ответ:'))
    score = 0
    if y == 2:
        print('Верно! Вы заработали 1/2 баллов.')
        a = 0
        b = 1
        if b >= a:
            print('Вы улучшили свой результат! Итоговый счет 1/2.')
    else:
        print('Неверно! Ваш счет - 0.')
        a = 0
        b = 0
        if a <= b:
            print('Вы не улучшили свой результат! Итоговый счет: 0/2.')

elif x > 4:
    print('Неверно! Ваш счет - 0.')
    print('У Вас есть вторая попытка!')
    y = int(input('Сколько равно 50/25? Введите ответ:'))
    score = 0
    if y == 2:
        print('Верно! Вы заработали 1/2 баллов.')
        a = 0
        b = 1
        if b >= a:
            print('Вы улучшили свой результат! Итоговый счет 1/2.')
    else:
        print('Неверно! Ваш счет - 0.')
        a = 0
        b = 0
        if a <= b:
            print('Вы не улучшили свой результат! Итоговый счет: 0/2.')

