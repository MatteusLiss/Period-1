import random as rand

urna = list(range(1, 35 + 1))
lottorad = []

for i in range(0, 7):
    index = rand.randint(0, 34-i)
    slumpat_tal = urna.pop(index)
    lottorad.append(slumpat_tal)

print(sorted(lottorad))