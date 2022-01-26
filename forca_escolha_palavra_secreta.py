
def gerador_10_palavras_portugues():
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    import unidecode
    # import PySimpleGUI as sg
    import threading
    import time

    def escolha_categoria():
        global categoria_escolhida
        categoria_escolhida = input('''
                Escolha uma das opções de categoria abaixo:
    
                0: Sem Categoria 
                1: Cores
                2: Alimentos
                3: Animais
                4: Profissões
                5: Transporte
                6: Corpo Humano
    
                Digite a opção escolhida: ''')
        global dic
        dic = {'0': '1',
               '1': '4',
               '2': '2',
               '3': '3',
               '4': '12',
               '5': '13',
               '6': '5'}
        time.sleep(1)
        print('''\n
                ESCOLHENDO A PALAVRA SECRETA. AGUARDE...''')

    threading.Thread(target=escolha_categoria()).start()

    def webscrapping(categoria_escolhida, dic):
        url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=10"
        if categoria_escolhida == 0:
            url = url
        else:
            for k, n in dic.items():
                if categoria_escolhida == k:
                    categoria_escolhida = n
                    break
            url = url + "&fs2=" + categoria_escolhida
        # lista_categorias = ['SEM CATEGORIA', 'ALIMENTOS', 'ANIMAIS', 'CORES', 'CORPO HUMANO']
        # sg.popup_quick_message(f'CATEGORIA ESCOLHIDA: {lista_categorias[int(categoria_escolhida)-1]}',
        # font=('Large', 10), button_type=5,
        #                        keep_on_top=True, relative_location=(-2000, -200), auto_close_duration=10)

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        teste = urlopen(req).read()
        data = teste.decode('utf-8')  # Precisa de decodificação para que os acentos apareçam
        soup = BeautifulSoup(data, "html.parser")
        data1 = soup.find_all('div')  # Encontra todas as tags <div> </div> e mostra em formato de lista
        words = data1[1:]  # pega somente os elementos da lista que contém as palavras geradas
        global lista
        lista = []
        for word in words:
            palavra2 = str(word)
            palavra2 = palavra2[43:-6].strip()
            palavra2 = unidecode.unidecode(palavra2)
            if palavra2 == '' or ' ' in palavra2:
                continue
            lista.append(palavra2)

    threading.Thread(target=webscrapping(categoria_escolhida, dic)).start()

    return lista


def gerador_de_palavras_para_forca():
    import random
    lista = gerador_10_palavras_portugues()

    palavra_secreta = random.choice(lista)
    # ARMAZENAMENTO EM UM ARQUIVO DA PALAVRA QUE SERÁ UTILIZADA COMO PALAVRA-SECRETA:
    try:
        nome_arquivo = 'palavra_chave_arquivo'
        arquivo = open(nome_arquivo, 'r+')
        arquivo.truncate(0)
        arquivo.writelines(f'{palavra_secreta.upper()}')
    # Caso não exista o arquivo, ele será criado
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(f'{palavra_secreta.upper()}')
    return palavra_secreta
