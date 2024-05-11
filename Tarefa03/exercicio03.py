# Curso basico de python
# Nome do desenvolvedor: Leandro Reichardt Alcantara
# versão 1.0
# exercicio de logica de programação
# com a logica de programação em python
# Exercicio para informar o percentual de desconto que o usuario vai soliciar

valor = float(input("escreva o valor do item "))

desconto = float(input("escreva o percentual de desconto deste item "))

final= ((valor/100)*desconto)
valorDescontado = valor - final

print("o valor do item é :", valor, "o desconto é :", desconto, "o item fica :", valorDescontado)