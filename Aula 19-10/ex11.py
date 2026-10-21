vet = []
vetp = []
veti = []

for i in range(4):
    vet.append(int(input("Digite seus valores:")))
for i in range(4):
    if vet[i] % 2 == 0:
        vetp.append(vet[i])
    else:
        veti.append(vet[i])
print("Números Pares:",vetp)
print("Números Impares:",veti)