x = float(input())
y = float(input())
z = str(input())
if z == '+':
    print(x + y)
if z == '-':
    print(x - y)
if z == '*':
    print(x * y)
if z == '/':
    if y > 0:
        print(x / y)
    else:
        print('Деление на 0!')
if z == 'mod':
    if y > 0:
        print(x % y)
    else:
        print('Деление на 0!')
if z == 'pow':
    print(x ** y)
if z == 'div':
    if y > 0:
        print(x // y)
    else:
        print('Деление на 0!')



