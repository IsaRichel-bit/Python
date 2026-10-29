def salario(a,b):
    if (a > 40):
        horaExtra = a - 40
        return 40 * b + horaExtra * b * 1.5
    else:
        return a * b
        

x = float(input("Digite suas horas trabalhadas:"))
y = float(input("Digite seu salario:"))
resp = salario(x,y)
print("Seu salario é:",resp)
