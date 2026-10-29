def p(vet):
    if (vet == vet[::-1]):
        print("Essa palavra escrita é um palindromo!")
    else:
        print("Essa palavra não é um palindromo!")
    return vet

x = str(input("Digite uma palavra,frase ou número:"))
resp = p(x)
print("Seu palindromo é:",resp)