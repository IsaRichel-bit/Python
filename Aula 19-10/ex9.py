vet = []
vetf = []

for i in range(3):
    vet.append(int(input("Digite seus valores:")))
    if i % 2 == 0:
        vetf.append(vet[i]*2)
        print(vetf[i])
    else:
        vetf.append(vet[i])
        print(vetf[i]*3)