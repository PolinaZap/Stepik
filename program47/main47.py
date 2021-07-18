dna = input()
score = 1
z = 0
while z + 1 < len(dna):
    if dna[z] == dna[z + 1]:
        score += 1
    else:
        print(dna[z] + str(score), end='')
        score = 1
    z += 1
print(dna[z] + str(score))