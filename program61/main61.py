# три способа вернуть список в обратном порядке
a = [5, 10, 6]

a.reverse() # изменяет список
print(a)

reversed(a) # не изменяет изначальный список
print(a)

a[::-1] # не изменяет изначальный список
print(a)