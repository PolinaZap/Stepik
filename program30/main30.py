'''
print this painting:
*

**

***

****

*****

******
...

'''
x = int(input('Enter how mane strings do you want:'))
y = '*'
while len(y) <= x:
    print(y)
    y += '*'