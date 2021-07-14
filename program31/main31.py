# print sum of number from your number a to your number b
a = int(input('Enter any number:'))
b = int(input('Enter any number:'))
sum = 0
x = a
while x <= b:
    sum += x
    x += 1
print(sum)