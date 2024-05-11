# Curso basico de python
# Nome do desenvolvedor: Leandro Reichardt Alcantara
# versão 1.0
# exercicio de logica de programação
# com a logica de programação em python
# Exercicio para calcular dias, horas e minutos em segundo

#dias = 86400
#horas = 3600
#minuto = 60
#segundos = 1

dias= int(input("digite a quantidade de dias "))
horas = int(input("Digite a quantidade de horas "))
minutos= int(input("digite a quantidade de minutos "))
segundos= int(input("digite a quantidade de segundos "))

calculo = (dias*86400) + (horas*3600) + (minutos*60) + (segundos*1)

print ("A quantidade de segundos é :", calculo)