
numero = int(input("Digite um número (-1 para terminar): "))

while numero != -1:
    print("Tabuada do", numero)

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    numero = int(input("Digite outro número (-1 para terminar): "))

print("Programa encerrado!")
