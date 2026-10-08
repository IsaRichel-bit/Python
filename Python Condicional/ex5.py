A = int(input("Digite N1:"))
B = int(input("Digite N2:"))
C = int(input("Digite N3:"))

if A>B and B>C:
    print("A ordem é:",A,B,C)
elif A>C and C>B:
    print("A ordem é:",A,C,B)
elif B>A and A>C:
    print("A ordem é:",B,A,C)
elif B>C and C>A:
    print("A ordem é:",B,C,A)
elif C>A and A>B:
    print("A ordem é:",C,A,B)
else:
    print("A ordem é:",C,B,A)