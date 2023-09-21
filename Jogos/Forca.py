import random


def jogar1():
    mensagem_de_abertura()
    palavra_secreta = escolhe_a_palavra_secreta()

    letras_acertadas = acertos_do_jogador(palavra_secreta)
    print(letras_acertadas)

    print(palavra_secreta)

    acertou = False
    enforcou = False
    tentativas = 0

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:

        chute = chute_do_usuario()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            print('Você errou, tentativa {} de 6'.format(tentativas))
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)



    if acertou:
        mesagem_de_vitoria()
    else:
        mensagem_de_derrota(palavra_secreta)



def mensagem_de_abertura():
    print("*************************************")
    print("*    Bem vindo ao jogo da Forca!    *")
    print("*************************************")

def escolhe_a_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def acertos_do_jogador(palavra):
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas

def chute_do_usuario():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()  # Remove os espeaços (strip) e Transforma as letras minúsculas em maiusculas (upper)
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1

def mesagem_de_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_de_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

# utilizado para executar o jogo sem passar pela escolha
if __name__ == "__main__":
    jogar1()