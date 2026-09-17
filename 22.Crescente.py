V1=int(input("Digite o primeiro valor: "))
V2=int(input("Digite o segundo valor: "))

if V1>V2:
    print("Em ordem ficará:", V2, V1)
elif V1==V2:
    print("Os valores são iguais")
else:
    print("Em ordem ficará:", V1, V2)
