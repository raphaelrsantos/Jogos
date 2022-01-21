import time
import PySimpleGUI as sg
import os

# Atualizando o texto a ser utilizado como definidor do tempo:
arquivo = open('TEMPO', 'w+')
arquivo.truncate(0)
t1 = int(sg.popup_get_text('TEMPO DO JOGO EM MINUTOS: ', location=(-1500, 150)))*60
# t = t1 * 60
arquivo.writelines(f'{t1}')


def countdown(num_of_secs):
    while num_of_secs:
        # Verificação se o jogo ainda está ativo (leitura do "semáforo")
        # arquivo = open('SEMAFORO', 'r+')
        # semaforo = arquivo.readline()
        # if semaforo == 'FINALIZAR PROGRAMA':
        #     break
        # Funcionamento do cronomêtro:
        m, s = divmod(int(num_of_secs), 60)
        f'{m:02d}:{s:02d}'
        time.sleep(1)
        num_of_secs -= 1
        sg.popup_quick_message(num_of_secs, font=('Large', 80), button_type=5,
                               keep_on_top=True, relative_location=(-1200, 500))
        # caso o tempo se esgote:
        if num_of_secs == 0:
            print('\nTEMPO ESGOTADO! APERTE QUALQUER TECLA PARA SAIR!' * 10)



arquivo = open('TEMPO', 'r+')
tempo = arquivo.readline()
print(tempo)
if tempo.isdigit():
    countdown(int(tempo))
else:
    print(f'O texto do arquivo é:--> {tempo} <-- VAZIO!')
    print('CRONOMETRO NÃO ESTÁ FUNCIONADO!!!\n' * 5)



