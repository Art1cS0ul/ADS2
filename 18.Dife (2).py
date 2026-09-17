V1=int(input("Digite o primeiro valor: "))
V2=int(input("Digite o segundo valor: "))
Sub=V1-V2
Sub2=V2-V1

if V1<V2:
    print("A diferença do primeiro valor para o segundo é de:", Sub2)
elif V1==V2:
    print("Os valores são iguais")
else:
    print("A diferença do primeiro valor para o segundo é de:", Sub)
