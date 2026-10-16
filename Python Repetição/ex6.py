
tinto = 0
branco = 0
rose = 0

tipo = input("Digite T, B, R ou F para finalizar: ")

while tipo != "F":
    if tipo == "T":
        tinto = tinto + 1
    elif tipo == "B":
        branco = branco + 1
    elif tipo == "R":
        rose = rose + 1
    else:
        print("Tipo inválido!")

    tipo = input("Digite T, B, R ou F para finalizar: ")

total = tinto + branco + rose

if total > 0:
    print(f"Total de vinhos: {total}")
    print(f"Tintos: {tinto / total * 100:.2f}%")
    print(f"Brancos: {branco / total * 100:.2f}%")
    print(f"Rosés: {rose / total * 100:.2f}%")
else:
    print("Nenhum vinho foi informado.")
