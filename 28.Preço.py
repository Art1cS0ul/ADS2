Preco=float(input("Digite o preço atual do produto: "))
Venda=float(input("Digite a média mensal de vendas: "))

if Venda<500 and Preco<30:
    Novo=Preco+(Preco*0.10)
elif Venda>=500 and Venda<1000 and Preco>=30 and Preco<80:
    Novo=Preco+(Preco*0.15)
elif Venda>=1000 and Preco>=80:
    Novo=Preco-(Preco*0.05)
else:
    Novo=Preco

print("O novo preço será de:", Novo)
