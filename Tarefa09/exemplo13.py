def soma():
    valor1 = int(input("escreva o primeiro valor "))
    valor2 = int(input("escreva o segundo valor "))
    print ("a soma é :", valor1+ valor2)


def subtracao():
    valor1 = int(input("escreva o primeiro valor "))
    valor2 = int(input("escreva o segundo valor "))
    print ("a subtração é :", valor1- valor2)


def multiplicacao():
    valor1 = int(input("escreva o primeiro valor "))
    valor2 = int(input("escreva o segundo valor "))
    print ("a multiplicação é :", valor1 * valor2)


def divisao():
    valor1 = int(input("escreva o primeiro valor "))
    valor2 = int(input("escreva o segundo valor "))
    print ("a divisão é :", valor1 / valor2)

def operacoes():
    escolha= int(input("Qual função você quer realizar? 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão "))
    if escolha == 1:
        soma()
    
    elif escolha == 2:
        subtracao()
    
    elif escolha == 3:
        multiplicacao()

    elif escolha == 4:
        divisao()
    
    else:
        print("Digite um numero valido")
        operacoes()
        
operacoes()