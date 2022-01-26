import time
import PySimpleGUI as sg


def countdown(num_of_secs):
    while num_of_secs:
        # VERIFICAÇÃO SE O JOGO AINDA ESTÁ ATIVO (LEITURA DO "SEMÁFORO")
        arquivo = open('SEMAFORO', 'r+')
        semaforo = arquivo.readline()
        if semaforo == 'FINALIZAR PROGRAMA':
            break
        # FUNCIONAMENTO DO CRONOMÊTRO:
        m, s = divmod(int(num_of_secs), 60)
        f'{m:02d}:{s:02d}'
        time.sleep(1)
        num_of_secs -= 1
        sg.popup_quick_message(num_of_secs, font=('Large', 80), button_type=5,
                               keep_on_top=True, relative_location=(-1200, 500))
        # caso o tempo se esgote:
        if num_of_secs == 0:
            print('\nTEMPO ESGOTADO! APERTE QUALQUER TECLA PARA SAIR!' * 10)
    # ESGOTADO O TEMPO, O "SEMÁFORO" É ATUALIZADO:
    arquivo = open('SEMAFORO', 'w+')
    arquivo.truncate(0)
    arquivo.writelines(f'FINALIZAR PROGRAMA')


arquivo = open('TEMPO', 'r+')
tempo = arquivo.readline()
countdown(int(tempo))


