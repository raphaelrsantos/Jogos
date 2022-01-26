import forca_main
import adivinhacao
import par_ou_impar


def escolhe_jogo():
    print()
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    print("(1) Forca \n"
          "(2) Adivinhação \n"
          "(3) Par ou Impar")
    print()
    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        forca_main.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
    elif jogo == 3:
        par_ou_impar.jogar()


if __name__ == "__main__":
    escolhe_jogo()
