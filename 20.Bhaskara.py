A=int(input("Digite o valor de A: "))
B=int(input("Digite o valor de B: "))
C=int(input("Digite o valor de C: "))

delt=(B**2-4*A*C)
UmaR=(-B/(2*A))
R1=((-B+(delt**0.5))/(2*A))
R2=((-B-(delt**0.5))/(2*A))

if delt==0:
      print("Há apenas uma raiz, de valor:", UmaR)
elif delt<0:
    print("Não há raízes reais")
else:
    print("As raízes são:", R1, "e", R2)

    
