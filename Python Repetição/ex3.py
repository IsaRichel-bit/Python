soma = 0
contador = 0

for i in range(10):
    N = int(input("Digite um número:"))

    if N % 2 == 0:
        soma = soma + N
        contador = contador + 1
if contador > 0:
        media = soma / contador
        print(f"A média é::{media:.2f}")
else:
        print("Nenhum número par foi digitado")