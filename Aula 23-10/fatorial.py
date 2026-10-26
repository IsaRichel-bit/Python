def fatorial(num):
    fat = 1

    for i in range(1, num + 1):
        fat = fat * i
    return fat

x = (int(input("Digite um número:")))
resp = fatorial(x)
print("O Fatorial é:",resp)