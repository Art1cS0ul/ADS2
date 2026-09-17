Soma=0

for Num in range(1, 16):
    Den=Num*Num

    if Num%2==0:
        Soma=Soma-(Num/Den)
    else:
        Soma=Soma+(Num/Den)

print("O resultado da série é:", Soma)
