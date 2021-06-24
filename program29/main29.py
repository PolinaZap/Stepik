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
a = int(input('Enter how many strings do you want:'))
c = 1
while c <= a:
    print(c * '*')
    c += 1