def tabuada(n):
           for i in range(1,11):
               print(f"{n} x {i} = {n * i}")
def imc(x,y):
    return x/(y**2)


def fat(num):
            fat = 1
            for i in range(2, num + 1):
                fat = fat * i
            return fat
while True:
    opcao = int(input("Escolha uma opção:"))

    print("1: Tabuada de um número")
    print("2:Calculcar o IMC (Indice de Massa Muscular)")
    print("3:Calcular Fatorial")
    print("-1: Encerrar o Pograma")

    match opcao:
        case 1:
            x= int(input("Digite o número:"))
            tabuada(x)
        case 2:
            x = float(input("Digite seu peso:" ))
            y = float(input("Digite sua altura:"))
            print(f"{imc(x,y):.2f}")
        case 3:
            z = int(input("Digite seu número:"))
            fat(z)
            print(f"fatorial:{fat(z):.2f}")
        case -1: 
            print("Encerrado");
            break