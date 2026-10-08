A = float(input("Digite altura:"))
S = str(input("Digite seu sexo (M/F):"))

if S == "M":
    peso = (72.7*A)-58
    print("Seu peso ideal é:",peso)

elif S == "F":
    peso = (62.1*A)-44.7
    print("Seu peso ideal é:",peso)
