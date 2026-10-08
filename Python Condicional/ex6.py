L = float(input("Digite quantos litros você precisa:"))
T = str(input("Escolha seu combustivel (A/G):"))

if T == "A":
    if L<= 20:
        valor = L * 2.10
        desconto = valor * 0.03
    else:
        valor = L * 2.10
        desconto = valor * 0.05

elif T == "G":
    if  L<=20:
        valor = L * 3.30
        desconto = L * 0.04
    else:
        valor = L * 3.30
        desconto = L * 0.06
else:
    print("Combustivel Invalido")
    valor = 0
    desconto = 0

if T == "A" or "G":
    print("Valor a pagar é:R$", round(valor - desconto,2))
