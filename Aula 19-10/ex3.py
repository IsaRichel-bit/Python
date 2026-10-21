notas = []
quantidade = int(input("Digite seus quantidade"))
soma = 0
contador = 0
media = 0
for i in range (quantidade):
    notas.append(int(input("Digite sua nota:")))
    soma = soma + notas[i]
media = soma/ quantidade
for i in range (quantidade):
    if notas[i] > media:
        acumulador = acumulador + 1

print("A média é:",media)
print("Médias acima:",acumulador)