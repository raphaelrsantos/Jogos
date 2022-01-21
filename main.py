import os
import threading
import escolha_palavra_secreta
import PySimpleGUI as sg

linha = '-' * 200
titulo = ' JOGO DA FORCA '
print()
print(linha)
print(titulo.center(200, '*'))
print(linha)

# Atualizando o texto a ser utilizado como definidor do tempo:
arquivo = open('TEMPO', 'w+')
arquivo.truncate(0)
t1 = int(sg.popup_get_text('TEMPO DO JOGO EM MINUTOS: ', location=(-1500, 150)))*60
arquivo.writelines(f'{t1}')

# Atualizando o texto a ser utilizado como semáforo para encerramento das threads
arquivo = open('SEMAFORO', 'w+')
arquivo.truncate(0)
arquivo.writelines(f'INICIAR PROGRAMA')


# criação e execução das threads:
def inicia_script(arquivo):
    os.system(f'py -3.9 {arquivo}')


processo1 = threading.Thread(target=inicia_script, args=('forca.py',))
processo2 = threading.Thread(target=inicia_script, args=('cronometro.py',))

escolha_palavra_secreta.gerador_de_palavras_para_forca()  # escolha da palavra-secreta para o jogo da FORCA
processo1.start()
processo2.start()
