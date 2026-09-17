V1=int(input("Digite o primeiro valor: "))
V2=int(input("Digite o segundo valor: "))

if V2<=V1:
    print("O segundo valor deve ser maior que o primeiro")

else:
    V3=int(input("Digite o terceiro valor: "))

    if V3<=V2:
        print("O terceiro valor deve ser maior que o segundo")

    else:
        V4=int(input("Digite o quarto valor: "))
            
    if V4<=V1:
        print(V4, V1, V2, V3)
    elif V4<=V2:
        print(V1, V4, V2, V3)
    elif V4<=V3:
        print(V1, V2, V4, V3)
    else:
        print(V1, V2, V3, V4)
    
