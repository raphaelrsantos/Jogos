import PySimpleGUI as sg

enforcou = False
ganhou = False
errou = 0
# Buscando a palavra secreta gerada pelo script "escolha_palavra_secreta.py"
arquivo = open('palavra_chave_arquivo', 'r+')
palavra_secreta = arquivo.readline()
mostrador = list(palavra_secreta)

img = "forca_inicio.png"
title = 'JOGO DA FORCA'
sg.popup_auto_close(f'CLIQUE NA TELA E SIGA COM O JOGO!', font=('Large', 10),
                    button_type=5,
                    keep_on_top=True, relative_location=(-2000, -50), auto_close_duration=2)
sg.PopupQuick(f'ERROS: {errou} de um total de 6.', title=title, text_color='#F7F6F2',
              keep_on_top=True,
              image=img, relative_location=(-1200, 100), auto_close_duration=3)
# Criação do mostrador:
for letra in range(0, len(mostrador)):
    mostrador[letra] = "_"

while not enforcou and not ganhou:
    print('\n \n')
    print('Palavra secreta: ', end='')
    # Mostrador na tela:
    for i in range(0, len(mostrador)):
        print(mostrador[i], end=' ')
    print("\n")

    # TENTATIVA DO USUÁRIO:
    chute = input("Qual letra? ").upper()

    # VERIFICAÇÃO CONSTANTE SE O CRONOMETRO NÃO ESTOUROU O PRAZO:
    arquivo = open('SEMAFORO', 'r+')
    semaforo = arquivo.readline()
    if semaforo == 'FINALIZAR PROGRAMA':
        # Abre o video do cachorro rindo:
        sg.shell_with_animation('cachorro_rindo.mp4', location=(-1000, 100))
        break

    cont_parc = 0
    for i in range(0, len(palavra_secreta)):
        if chute == palavra_secreta[i]:
            mostrador[i] = chute
        else:
            cont_parc += 1
        if cont_parc == len(palavra_secreta):
            print("Errou! Tente novamente \n")
            errou += 1
            # Mostra a forca avançando:
            sg.PopupQuick(f'ERROS: {errou} de um total de 6.', title=title, text_color='#F7F6F2',
                          keep_on_top=True,
                          image=f'forca_{errou}erros.png', relative_location=(-1200, 100),
                          auto_close_duration=2)
    # PERDEU O JOGO:
    if errou == 6:
        # Abre o video do cachorro rindo:
        sg.shell_with_animation('cachorro_rindo.mp4', location=(-1000, 100))
        print("VOCÊ PERDEU! ERROU 6 VEZES!")
        # Mostra a forca finalizada:
        sg.popup_auto_close(title=title, text_color='#F7F6F2', keep_on_top=True,
                            image=f'forca_perdeu.png', relative_location=(-1200, 100), auto_close_duration=2)
        enforcou = True
        arquivo = open('SEMAFORO', 'w+')
        arquivo.truncate(0)
        arquivo.writelines(f'FINALIZAR PROGRAMA')
        break

    # VENCEU O JOGO:
    if mostrador == list(palavra_secreta):
        print('\n \n')
        print('Palavra secreta: ', end='')
        for i in range(0, len(mostrador)):
            print(mostrador[i], end=' ')
        print("\n")
        sg.popup_auto_close(f'PARABÉNS! VOCÊ VENCEU O JOGO!!!', font=('Large', 10),
                            button_type=5,
                            keep_on_top=True, relative_location=(-2000, -50), auto_close_duration=3)
        # Mostra o video de comemoração:
        sg.shell_with_animation('comemora0.mp4', location=(-1200, 100), keep_on_top=True,)
        ganhou = True
        arquivo = open('SEMAFORO', 'w+')
        arquivo.truncate(0)
        arquivo.writelines(f'FINALIZAR PROGRAMA')
        break

print()
print("FIM DO JOGO \n")
if enforcou:
    # Mostra a palavra secreta:
    sg.popup_auto_close(f'PALAVRA SECRETA: "{palavra_secreta.upper()}"', title=title, font=('Large', 30),
                        button_type=5, text_color='#F7F6F2',
                        keep_on_top=True, relative_location=(-1600, 100),
                        auto_close_duration=3)


