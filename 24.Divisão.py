Num=int(input("Digite o valor a ser verificado: "))
Div=Num%2
Div2=Num%3
Qt=Num/2
Qt2=Num/3


if Div==0 and Div2==0:
    print("É divisível por 2 e por 3, sendo que por 2 é", Qt, "e por 3", Qt2)
elif Div==0 and Div2!=0:
    print("É divisível apenas por 2")
elif Div==2 and Div!=0:
    print("É divisível apenas por 3")
else:
    print("Não é divisível por 2 e 3")
