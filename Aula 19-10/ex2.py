vet = []
quantidade = int(input("Digite seus quantidade"))
soma = 0
somapar =0
contador = 0
media = 0
for i in range (quantidade):
    vet.append(int(input("Digite os números do vetores")))
    soma = soma + vet[i]
    if vet[i] % 2 == 0:
        somapar = somapar + vet[i]
        contador += 1
if contador > 0:
    media = somapar / contador
    print(media)
