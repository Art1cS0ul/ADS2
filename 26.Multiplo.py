M1=int(input("Digite o primeiro valor: "))
M2=int(input("Digite o segundo valor: "))

if M1==0 or M2==0:
    print("Não é possível verificar múltiplo com zero")
else:
    Divs=M1%M2
    Divs2=M2%M1

    if M1>=M2 and Divs==0:
        print("O número", M1, "é múltiplo de", M2)
    elif M2>=M1 and Divs2==0:
        print("O número", M2, "é múltiplo de", M1)
    else:
        print("Não são múltiplos")
