vet = []
quantidade = int(input("Digite seus quantidade"))
soma = 0
for i in range (quantidade):
    vet.append(int(input("Digite os números do vetores")))
    soma = soma + vet[i]
print(soma)