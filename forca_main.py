
def jogar():
    import os
    import threading
    import forca_escolha_palavra_secreta
    import PySimpleGUI as sg
    from time import sleep

    linha = '-' * 200
    titulo = ' JOGO DA FORCA '
    print()
    print(linha)
    print(titulo.center(200, '*'))
    print(linha)

    # ATUALIZANDO O TEXTO A SER UTILIZADO COMO DEFINIDOR DO TEMPO:
    with open('TEMPO', 'w+') as arquivo:
        arquivo.truncate(0)
        t1 = int(sg.popup_get_text('TEMPO DO JOGO EM MINUTOS: ', location=(-1500, 400))) * 60
        arquivo.writelines(f'{t1}')
    # arquivo.close()  # teria q fechar o arquivo para o ponteiro da proxima leitura não iniciar já no final da string,
    # porém com a instrução "with open..." o próprio Python abre e fecha o arquivo

    # ATUALIZANDO O TEXTO A SER UTILIZADO COMO SEMÁFORO PARA ENCERRAMENTO DAS THREADS
    arquivo = open('SEMAFORO', 'w+')
    arquivo.truncate(0)
    arquivo.writelines(f'INICIAR PROGRAMA')
    arquivo.close()

    # CRIAÇÃO E EXECUÇÃO DAS THREADS:
    def inicia_script(arquivo):
        os.system(f'py -3.9 {arquivo}')

    forca_escolha_palavra_secreta.gerador_de_palavras_para_forca()  # escolha da palavra-secreta para o jogo da FORCA
    processo1 = threading.Thread(target=inicia_script, args=('forca_cronometro.py',))
    processo2 = threading.Thread(target=inicia_script, args=('forca_exec.py',))
    processo1.start()
    sleep(1)
    processo2.start()
