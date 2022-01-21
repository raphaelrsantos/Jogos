

def gerador_10_palavras_portugues():
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    import unidecode
    import PySimpleGUI as sg

    url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=10"

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

    dic = {'0': '1',
           '1': '4',
           '2': '2',
           '3': '3',
           '4': '12',
           '5': '13',
           '6': '5'}

    if categoria_escolhida == 0:
        url = url
    else:
        for k, n in dic.items():
            if categoria_escolhida == k:
                categoria_escolhida = n
        url = url + "&fs2=" + categoria_escolhida
    # lista_categorias = ['SEM CATEGORIA', 'ALIMENTOS', 'ANIMAIS', 'CORES', 'CORPO HUMANO']
    # sg.popup_quick_message(f'CATEGORIA ESCOLHIDA: {lista_categorias[int(categoria_escolhida)-1]}', font=('Large', 10), button_type=5,
    #                        keep_on_top=True, relative_location=(-2000, -200), auto_close_duration=10)
    sg.popup_auto_close(f'AGUARDE: ESCOLHENDO A PALAVRA SECRETA....', font=('Large', 10),
                           button_type=5,
                           keep_on_top=True, relative_location=(-2000, -50), auto_close_duration=2)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    teste = urlopen(req).read()
    data = teste.decode('utf-8')  # Precisa de decodificação para que os acentos apareçam
    soup = BeautifulSoup(data, "html.parser")
    data1 = soup.find_all('div')  # Encontra todas as tags <div> </div> e mostra em formato de lista
    words = data1[1:]  # pega somente os elementos da lista que contém as palavras geradas

    lista = []
    for word in words:
        palavra2 = str(word)
        palavra2 = palavra2[43:-6].strip()
        palavra2 = unidecode.unidecode(palavra2)
        if palavra2 == '' or ' ' in palavra2:
            continue
        lista.append(palavra2)

    return lista


def gerador_de_palavras_para_forca():
    lista = gerador_10_palavras_portugues()
    palavra_secreta = lista[0]
    # Armazenamento em um arquivo da palavra que será utilizada como palavra-secreta:
    try:
        nome_arquivo = 'palavra_chave_arquivo'
        arquivo = open(nome_arquivo, 'r+')
        arquivo.truncate(0)
        arquivo.writelines(f'{palavra_secreta.upper()}')
    # Caso não exista o arquivo, ele deverá ser criado
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(f'{palavra_secreta.upper()}')
    return palavra_secreta


