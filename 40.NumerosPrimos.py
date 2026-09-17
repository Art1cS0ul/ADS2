V1=int(input("Digite o primeiro valor: "))
V2=int(input("Digite o segundo valor: "))

if V1>V2:
    Maior=V1
    Menor=V2
else:
    Maior=V2
    Menor=V1

for Num in range(Menor, Maior+1):
    if Num>1:
        Div=0

        for Cont in range(1, Num+1):
            if Num%Cont==0:
                Div=Div+1

        if Div==2:
            print(Num)
