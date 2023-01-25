import random
print("\n\nJogo da adivinhação\n")
rodada = 1
totalDeRodadas = 0
numero_secreto = random.randint(1, 31)

print(numero_secreto)

print("Qual nível de dificuldade?")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("\nDefina o nível: "))

if(nivel == 1):
    totalDeRodadas = 20
elif (nivel == 2):
    totalDeRodadas = 10
elif (nivel == 3):
    totalDeRodadas = 5
else:
    print("\nInválido, sua dificuldade foi automaticamente selecionada como media")
    totalDeRodadas = 10


chute = int(input("\n\nDigite o seu chute (de 1 a 30) você tem {} tentativas: \n".format(totalDeRodadas)))


for rodada in range (0, totalDeRodadas+1):
    if (numero_secreto > chute):
        print("\nO seu chute de {:.0f} foi menor\n".format(chute) )
        chute = int(input("Digite o seu chute (de {:.0f} a 30, rodada {:.0f}): ".format(chute,rodada)))
    elif (numero_secreto < chute):
        print("\nO seu chute de {:.0f} foi maior\n".format(chute) )
        chute = int(input("Digite o seu chute (de 1 a {:.0f}, rodada {:.0f}): ".format(chute,rodada)))
    elif(numero_secreto == chute):
        print("\n\nParabéns você acertou o número!\n\n")
        break
    rodada +=1    