import adivinhacao 
import forca 

print("\n\nEscolha o seu jogo\n")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("\nJogando forca\n")
    forca.jogarForca()

elif (jogo == 2):
    print("\nJogando adivinhação\n")
    adivinhacao.jogarAdivinhacao()