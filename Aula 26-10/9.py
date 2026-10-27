def validor(cpf):
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return True
    
    s = 0
    for i in range(9):
        s = s + int(cpf[i])* (10 - i)
    resto = s % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    s = 0
    for i in range(10):
        s = s + int(cpf[i]) *(11 - i)
    resto = s % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False
        
cpf = input("Digite seu CPF:")

if cpf.isdigit() and validor(cpf):
    print("CPF Válido")
else:
    print("CPF Inválido!")