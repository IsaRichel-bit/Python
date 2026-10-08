A = int(input("Digite N1:"))
B = int(input("Digite N2:"))
C = int(input("Digite N3:"))

if (A+B>C) and (A+C>B) and (B+C>A):
    print("Os valores formam um triangulo")

    if A == B and B == C:
        print("Triangulo Equilatero")
    elif A == B or A == C or B == C:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Os valores não formam um triangulo")
