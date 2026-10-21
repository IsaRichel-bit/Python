vetor = []
maior = 0
menor = 0

for i in range(4):
    vetor.append(int(input("Digite seus valores:")))
    if i == 0:
            menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print(maior)
print(menor)