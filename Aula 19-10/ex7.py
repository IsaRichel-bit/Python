N = int(input("Digite a quantidade de números:"))

vetor = []
for i in range(N):
    if i == 0 or i == 1:
        vetor.append(1)
    else:
        vetor.append(vetor[i-1]+vetor[i-2])
print(vetor)
