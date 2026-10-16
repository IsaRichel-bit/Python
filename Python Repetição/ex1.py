soma = 0

for numero in range(1,500):
    if numero % 2 != 0 and numero % 3 == 0:
        soma = soma + numero

print(soma)