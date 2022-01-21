import time
import PySimpleGUI as sg


def countdown(num_of_secs):
    while num_of_secs:
        # Verificação se o jogo ainda está ativo (leitura do "semáforo")
        arquivo = open('SEMAFORO', 'r+')
        semaforo = arquivo.readline()
        if semaforo == 'FINALIZAR PROGRAMA' or semaforo == 'VOLTAR AO MENU':
            break
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
    # Esgotado o tempo, o "semáforo" é atualizado:
    arquivo = open('SEMAFORO', 'w+')
    arquivo.truncate(0)
    arquivo.writelines(f'FINALIZAR PROGRAMA')


arquivo = open('TEMPO', 'r+')
tempo = arquivo.readline()
countdown(int(tempo))


