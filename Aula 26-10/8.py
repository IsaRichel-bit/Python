def somatoria(n):
    s = 0
    for i in range(1, n+1):
        s = s + i / (i **2)
    return s

x = int(input("Digite um número:"))
resp = somatoria(x)
print("A somatoria é:",resp)
    