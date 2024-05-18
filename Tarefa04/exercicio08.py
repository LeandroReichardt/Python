valor = int(input("Quantas maças você quer comprar? "))

if valor < 12:
    resultado = valor*1.30
    print("O valor fica ", resultado)

else:
    resultado2 = valor*1.00
    print("O valor fica ", resultado2)