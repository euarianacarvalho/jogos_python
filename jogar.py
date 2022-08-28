import adivinhacao
import forca

print("********************************")
print("******* Escolha um Jogo ********")
print("********************************")

print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual Jogo? "))
if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()

