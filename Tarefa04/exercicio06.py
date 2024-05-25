valor = int(input("Digite um valor "))

if valor <= 1:
    print("O valor não é primo")

elif valor%2 == 0 and valor!= 2 :
    print("o valor não é primo")

elif valor%3 == 0 and valor != 3 or valor%5 == 0 and valor != 5 or valor%7 == 0 and valor != 7:
    print("O valor não é primo")

else:
    print("o valor é primo")