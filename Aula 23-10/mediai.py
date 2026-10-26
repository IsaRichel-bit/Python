def media(vet):
    m = 0
    s = 0
    contador = 0
    for i in range(10):
        if i % 2 != 0:
            contador += 1
            s = s + vet[i]
    m = s / contador
    return m
        

vet = []
for i in range(10):
    vet.append(int(input("Número:")))
resp = media(vet)
print("A média é:",resp)