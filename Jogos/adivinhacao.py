print("**********************************")
print("Bem vindo ao jogo de Adivinhação!!")
print("**********************************")

numero_secreto= 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero:")
    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if(maior):
            print("Você errou!! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou! Oseu chute foi menor que o numero secreto")

    rodada = rodada + 1



