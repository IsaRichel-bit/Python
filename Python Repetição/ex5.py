
numero = int(input("Digite o número imaginado: "))
tentativas = 0

chute = int(input("Tente adivinhar o número: "))

while chute != numero:
    tentativas = tentativas + 1

    if chute > numero:
        print("Seu chute foi alto!")
    else:
        print("Seu chute foi baixo!")

    chute = int(input("Tente novamente: "))

    tentativas = tentativas + 1

print("Parabéns! Você acertou!")
print("Total de tentativas:", tentativas)
