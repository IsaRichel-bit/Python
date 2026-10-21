vet = []
vetf = []

for i in range(3):
    vet.append(int(input("Digite seus valores:")))
for i in range(3):
    vetf.append(vet[2-i])

print("Vetor Original:",vet)
print("Vetor Invertido:",vetf)
