# ATENÇÃO! ESTE PACOTE NÃO ESTÁ SENDO UTILIZADO NO JOGO
# pacote baixado do Github para estudo e aproveitamento de parte do código

class GeradorPalavras:
    def __init__(self):
        self

    def gerador_completo(self):
        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup
        url = "http://www.palabrasaleatorias.com/"

        idioma_palavras = input('''
        Escolha uma das opções de idioma abaixo:
        
        1 - Português
        2 - Inglês
        3 - Italiano
        4 - Francês
        5 - Espanhol
        
        Digite a opção escolhida:''')

        if idioma_palavras == '1':
            idioma = 'palavras-aleatorias'
        elif idioma_palavras == '2':
            idioma = 'random-words'
        elif idioma_palavras == '3':
            idioma = 'parole-casuali'
        elif idioma_palavras == '4':
            idioma = 'mots-aleatoires'
        elif idioma_palavras == '5':
            idioma = 'index'

        n_palavras = input("\nDigite quantas palavras você quer que sejam geradas:")
        while int(n_palavras) > 10:  # Coloquei essa restrição apenas pq o site não deixava gerar mais de 10 palavras
            print('No máximo 10 palavras podem ser geradas. Escolha um valor menor.')
            n_palavras = input("\nDigite quantas palavras você quer que sejam geradas:")

        categoria_escolhida = input('''
        Escolha uma das opções de categoria abaixo:
        
        1 - Sem categoria
        2 - Alimentos
        3 - Animais
        4 - Profissões
        5 - Corpo Humano
        
        Digite a opção escolhida:''')

        if categoria_escolhida == 1:
            url = url + idioma + ".php?fs=" + n_palavras
        else:
            url = url + idioma + ".php?fs=" + n_palavras + "&fs2=" + categoria_escolhida

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
            if palavra2 == '':
                continue
            lista.append(palavra2)

        return lista

    def gerador_10_palavras_portugues(self):
        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup
        url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=10"

        categoria_escolhida = input('''
                Escolha uma das opções de categoria abaixo:

                1 - Sem categoria
                2 - Alimentos
                3 - Animais
                4 - Profissões
                5 - Corpo Humano

                Digite a opção escolhida:''')

        if categoria_escolhida == 1:
            url = url
        else:
            url = url + "&fs2=" + categoria_escolhida

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
            if palavra2 == '':
                continue
            lista.append(palavra2)

        return lista
