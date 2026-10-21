A = int(input("Digite um número de 3 dígitos: "))

centena = A // 100
dezena = (A // 10) % 10
unidade = A % 10

print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)

print("Número invertido:", unidade * 100 + dezena * 10 + centena)


