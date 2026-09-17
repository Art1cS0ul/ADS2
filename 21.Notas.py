N1=float(input("Registre a primeira nota: "))
N2=float(input("Registre a segunda nota: "))
N3=float(input("Registre a terceira nota: "))
N4=float(input("Registre a quarta nota: "))
Media=((N4+N3+N2+N1)/4)

if Media>=6.0:
    print("APROVADO")
elif Media>=3.0 and Media<6.0:
    print("EXAME")
else:
    print("RETIDO")
