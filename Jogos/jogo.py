import forca
import adivinhacao01

def  escolha_jogo():
    print("**********************************")
    print("*********Escolha seu jogo!!!!!****")
    print("**********************************")

    print("(1) - Forca")
    print("(2) - Adivimhação")


    jogo = int(input("Qual o jogo:"))

    if(jogo ==  1):
        print("Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhação")
        adivinhacao01.jogar()

if (__name__ == "__main__"):
    escolha_jogo()








