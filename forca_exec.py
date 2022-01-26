import PySimpleGUI as sg

# BUSCANDO A PALAVRA SECRETA GERADA PELO SCRIPT "ESCOLHA_PALAVRA_SECRETA.PY"
arquivo = open('palavra_chave_arquivo', 'r+')
palavra_secreta = arquivo.readline()

# INICIO DA INTERFACE GRÁFICA:
img = "imagens/img_forca_inicio.png"
title = 'JOGO DA FORCA'
sg.PopupQuick(f'CLIQUE NA TELA E SIGA COM O JOGO!', font=('Large', 20),
              button_type=5,
              keep_on_top=False, relative_location=(-2000, 30), auto_close_duration=2)
sg.PopupQuick(f'ERROS: 0 de um total de 6.', title=title, text_color='#F7F6F2',
              keep_on_top=True,
              image=img, relative_location=(-1200, 100), auto_close_duration=3)

# CRIAÇÃO DO MOSTRADOR (USANDO A TECNICA "List Comprehension"):
mostrador = ['_' for letra in range(0, len(palavra_secreta))]

# FORMA TRADICIONAL DE LOOP PARA A CRIAÇÃO DO MOSTRADOR:
# mostrador = list(palavra_secreta)
# for letra in range(0, len(mostrador)):
#     mostrador[letra] = "_"

# ATUALIZAÇÃO DO SEMÁFORO
def atualiza_semaforo():
    arquivo = open('SEMAFORO', 'w+')
    arquivo.truncate(0)
    arquivo.writelines(f'FINALIZAR PROGRAMA')

errou = 0
while True:
    print('\n \n')
    print('Palavra secreta: ', end='')
    # Mostrador na tela:
    for i in range(0, len(mostrador)):
        print(mostrador[i], end=' ')
    print("\n")

    # TENTATIVA DO USUÁRIO:
    chute = input("Qual letra?  RESPOSTA: ").upper()

    # VERIFICAÇÃO CONSTANTE SE O CRONOMETRO NÃO ESTOUROU O PRAZO:
    arquivo = open('SEMAFORO', 'r+')
    semaforo = arquivo.readline()
    if semaforo == 'FINALIZAR PROGRAMA':
        # ABRE O VIDEO DO CACHORRO RINDO:
        sg.shell_with_animation(r'C:\Users\Raphael\OneDrive\Documentos\PycharmProjects\Jogos\Videos\
        vid_cachorro_rindo.mp4', location=(-1000, 100))
        break

    # ANÁLISE DO CHUTE DO USUÁRIO:
    cont_parc = 0
    for i in range(0, len(palavra_secreta)):
        if chute == palavra_secreta[i]:
            mostrador[i] = chute
        else:
            cont_parc += 1
        if cont_parc == len(palavra_secreta):
            print("Errou! Tente novamente \n")
            errou += 1
            # MOSTRA A FORCA AVANÇANDO:
            sg.PopupQuick(f'ERROS: {errou} de um total de 6.', title=title, text_color='#F7F6F2',
                          keep_on_top=True,
                          image=f'imagens/img_forca_{errou}erros.png', relative_location=(-1200, 100),
                          auto_close_duration=2)
    # PERDEU O JOGO:
    if errou == 6:
        atualiza_semaforo()
        # MOSTRA A FORCA FINALIZADA:
        sg.popup_quick_message(title=title, text_color='#F7F6F2', keep_on_top=True,
                               image=f'imagens/img_forca_perdeu.png', relative_location=(-1200, 100),
                               auto_close_duration=2)
        sg.popup_auto_close(f' \n VOCÊ PERDEU! ERROU 6 VEZES!!! \n', font=('Large', 20),
                            button_type=5,
                            keep_on_top=True, relative_location=(-2000, -50), auto_close_duration=2)
        print("     _______________         ")
        print(r"   /               \       ")
        print(r"  /                 \      ")
        print(r"//                   \/\  ")
        print(r"\|   XXXX     XXXX   | /   ")
        print("  |   XXXX     XXXX   |/     ")
        print("  |   XXX       XXX   |      ")
        print("  |                   |      ")
        print(r" \__      XXX      __/     ")
        print(r"   |\     XXX     /|       ")
        print("    | |           | |        ")
        print("    | I I I I I I I |        ")
        print("    |  I I I I I I  |        ")
        print(r"   \_             _/       ")
        print(r"     \_         _/         ")
        print(r"       \_______/           ")
        # ABRE O VIDEO DO CACHORRO RINDO:
        sg.shell_with_animation(r'C:\Users\Raphael\OneDrive\Documentos\PycharmProjects\Jogos\Videos'
                                r'\vid_cachorro_rindo.mp4', location=(-1000, 100))

        # MOSTRA A PALAVRA SECRETA:
        sg.popup_auto_close(f'PALAVRA SECRETA: "{palavra_secreta.upper()}"', title=title, font=('Large', 30),
                            button_type=5, text_color='#F7F6F2',
                            keep_on_top=True, relative_location=(-1600, 100),
                            auto_close_duration=3)
        break

    # VENCEU O JOGO:
    if mostrador == list(palavra_secreta):
        atualiza_semaforo()
        print('\n \n')
        print('Palavra secreta: ', end='')
        for i in range(0, len(mostrador)):
            print(mostrador[i], end=' ')
        print("\n")
        sg.popup_auto_close(f' \n VOCÊ VENCEU O JOGO! PARABÉNS!!! \n', font=('Large', 20),
                            button_type=5,
                            keep_on_top=True, relative_location=(-2000, -50), auto_close_duration=2)
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print(r"    .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print(r"      \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        # MOSTRA O VIDEO DE COMEMORAÇÃO:
        sg.shell_with_animation(r'C:\Users\Raphael\OneDrive\Documentos\PycharmProjects\Jogos\Videos\vid_comemora0.mp4',
                                location=(-1200, 100), keep_on_top=True)
        ganhou = True
        break


print()
print("FIM DO JOGO \n")
