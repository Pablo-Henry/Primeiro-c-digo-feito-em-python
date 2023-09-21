#importação de biblioteca

import random

def jogar2():
    print("*************************************")
    print("* Bem vindo ao jogo de Adivinhação! *")
    print("*************************************")

    #função de arredondamento de valor e função utilizada para a criação de um número aleatório
    num_secreto = round(random.randrange(1, 101))
    print("Você possuí 3 tentativas")
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    #print(num_secreto)

    print("Escolha o nível de dificuldade desesejado: (1) Fácil  (2) Normal (3) Difícil")
    nivel_dificuldade = int(input(": "))

    if nivel_dificuldade == 1:
        total_de_tentativas = 20
    elif nivel_dificuldade == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while rodada <= total_de_tentativas:
        print("Tentaiva {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você escolheu o número {}: ".format(chute))
        if chute < 1 or chute > 100:
            print("Valor invalido! Digite um número entre 700 e 800")
            continue
        if chute == num_secreto:
            print("Você acertou! Quantidade de pontos feitos: {} ".format(pontos))
            break
        else:
            if chute > num_secreto:
                print("Você errou! O valor do seu chute é maior do que o valor do número secreto.")
            elif chute < num_secreto:
                print("Você errou! O valor do seu chute é menor do que o valor do número secreto.")
            rodada = rodada + 1
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do Jogo!")

#utilizado para executar o jogo sem passar pela escolha
if __name__ == "__main__":
    jogar2()