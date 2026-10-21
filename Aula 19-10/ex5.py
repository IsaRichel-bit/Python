vetor = []
vetor1 = []
soma = 0
for i in range (5):
    vetor.append(int(input("Digite seus valores:")))
for i in range(5):
    vetor1.append(int(input("Digite seu segundo valor:")))
for i in range (5):
    soma = vetor[i] + vetor1[i]
    print(soma)