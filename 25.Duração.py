HoraI=int(input("Digite a hora de início: "))
MinI=int(input("Digite os minutos de início: "))

HoraF=int(input("Digite a hora final: "))
MinF=int(input("Digite os minutos finais: "))

Inicio=(HoraI*60)+MinI
Fim=(HoraF*60)+MinF

if Fim>=Inicio:
    Duracao=Fim-Inicio
else:
    Duracao=(1440-Inicio)+Fim

Horas=Duracao//60
Minutos=Duracao%60

print("O tempo de jogo foi de", Horas, "horas e", Minutos, "minutos")
