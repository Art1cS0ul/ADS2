Num=int(input("Digite um número: "))
Soma=1
Fat=1

for Cont in range(1, Num+1):
    Fat=Fat*Cont
    Soma=Soma+(1/Fat)

print("O resultado da série é:", Soma)
