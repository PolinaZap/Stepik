'''
Дана геномная последовательность. Проверить, является ли она палиндромом.
    - строка является палиндромом, если она читается в обоих направлениях одинаково.
Мое решение:
'''
genome = input('Print any sting:').upper()
if genome == genome[::-1]:
    print('YES. This string is palindrome!')
else:
    print('NO. This string is not palindrome!')

