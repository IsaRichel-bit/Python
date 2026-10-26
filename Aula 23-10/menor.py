def funcao (a,b):

    if (a > b):
        print("{} é o menor valor." .format(b))
    elif (b > a):
        print("{} é o menor valor." .format(a))
    else:
        print("Os dois são iguais")

x = int(input("Valor 1:"))
y = int(input("Valor 2:"))
funcao(x,y)