Voltas=int(input("Digite o número de voltas: "))
Circuito=float(input("Digite a extensão do circuito em metros: "))
Tempo=float(input("Digite o tempo de duração em minutos: "))

Distancia=(Voltas*Circuito)/1000
Horas=Tempo/60

Velocidade=Distancia/Horas

print("A velocidade média foi de", Velocidade, "km/h")
