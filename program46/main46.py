'''
Дана геномная последовательность. Проверить, является ли она палиндромом.
    - строка является палиндромом, если она читается в обоих направлениях одинаково.
Решение на курсе | способ 3:
'''
s = input()
r = s[::-1]
if s == r:
    print('YES')
else:
    print('NO')