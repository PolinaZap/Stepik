x = int(input())
h = int(input())
m = int(input())
a = x // 60 + h
b = x % 60 + m
if b >= 60:
    a += 1
    b %= 60
print(a)
print(b)


