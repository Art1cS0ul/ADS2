V1=int(input("Digite o primeiro valor: "))
V2=int(input("Digite o segundo valor: "))
Soma=0

if V1>V2:
    Maior=V1
    Menor=V2
else:
    Maior=V2
    Menor=V1

for Num in range(Menor, Maior+1):
    if Num%2!=0:
        Soma=Soma+Num

print("A soma dos números ímpares é:", Soma)
