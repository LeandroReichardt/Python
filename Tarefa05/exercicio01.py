votosBrancos = int(input("Escreva a quantidade de votos brancos "))

votosNulos = int(input("Escreva a quantidade de votos nulos "))

votosValidos = int(input("Escreva a quantidade de votos validos "))

eleitores = votosBrancos + votosNulos + votosValidos

total = eleitores/100

print("O total de eleitores é :", eleitores)

print("O total de votos brancos são ",votosBrancos, "o percentual é ", votosBrancos*total)

print("O total de votos nulos são ",votosNulos, "o percentual é ", votosNulos*total)

print("O total de votos validos são ",votosValidos, "o percentual é ", votosValidos*total)