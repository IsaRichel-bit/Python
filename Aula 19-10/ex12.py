vet = []
soma = 0
media = 0
acima = 0
abaixo = 0

for i in range(5):
    vet.append(float(input("Digite seus valores:")))
    soma = soma + vet[i]

media = soma / 5

for i in range(5):
    if vet[i] > media *1.1:
        acima = acima + 1
    if vet[i] < media *1.1:
        abaixo = abaixo + 1

print("Média:",media)
print("Notas Acima:",acima)
print("Nota Abaixo:",abaixo)
