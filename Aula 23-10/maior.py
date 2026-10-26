def funcao (vet):
    maior = vet[0]

    for i in range(1,5):
        if (maior < vet[i]):
            maior = vet[i]
    return maior
vet = []
for i in range(5):
    vet.append(int(input("Números:")))
print("O maior é:" ,funcao(vet))

