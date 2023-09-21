import Forca
import Adivinhacao

def escolher_jogo():
    print("*************************************")
    print("*              Jogos!               *")
    print("*************************************")

    print("(1) Jogo da Forca  (2) Jogo de Adivinhação")

    jogo = int(input("Selecione o Jogo que deseja jogar: "))

    if jogo == 1:
        print("Abrindo Jogo da Forca!")
        Forca.jogar1()
    elif jogo == 2:
        print("Abrindo Jogo de adivinhação!")
        Adivinhacao.jogar2()

if __name__ == "__main__":
    escolher_jogo()