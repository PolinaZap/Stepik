# генерация списков

# выводит число несколько раз
a = [0] * 5
print(a)

# выводит число несколько раз
a = [5 for i in range(3)]
print(a)

# выводит квадраты целых чисел
a = [i * i for i in range(10)]
print(a)

# придает числам вид списка
a = [int(i) for i in input('Print numbers, use Spacebar:').split()]
print(a)