'''
print part of multiplication table;
a and b = the first and the past numbers of multiplier column;
c and d = the first and the past numbers of multiplier high string.
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for w in range(c, d + 1):
    print('\t', w, end='\t')
print()

for i in range(a, b + 1):
    print(i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, end='\t')
    print()