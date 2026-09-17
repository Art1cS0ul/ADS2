Num=int(input("Digite um número positivo: "))

Maior=Num
Menor=Num

for Cont in range(99):
    Num=int(input("Digite um número positivo: "))

    if Num>Maior:
        Maior=Num

    if Num<Menor:
        Menor=Num

print("O maior valor é:", Maior)
print("O menor valor é:", Menor)
