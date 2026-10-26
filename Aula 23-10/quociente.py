def quociente (a,b):
    contador = 0

    while a >= b:
        a = a - b
        contador += 1

    return contador

x = (float(input("Digite um número:")))
y = (float(input("Digite outro valor:")))

resp = quociente(x,y)
print("O quociente é:",resp)