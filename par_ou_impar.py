def jogar():
    print('-='*10, 'JOGO PAR OU ÍMPAR', '-='*10)
    from random import randint

    lista = ['P', 'I']
    num_pc = randint(1, 10)
    num = cont = 0
    result = 'vitoria'

    while result == 'vitoria':
        escolha = str(input('Escolha a opção par ou ímpar [P/I]: ').upper().strip()[0])
        while escolha not in 'PI':
            escolha = str(input('Escolha a opção par ou ímpar [P/I]: ').upper().strip()[0])
        num = int(input('Digite o número: '))
        print('>'*10)
        total = num + num_pc
        print(f'\nVocê jogou {num} e o computador jogou {num_pc}. Total = {total}.')
        print(f'\nDEU PAR! ' if total % 2 == 0 else 'DEU ÍMPAR! ', end='')
        if escolha == 'P':
            if total % 2 == 0:
                print(f'\nParabéns! Você venceu!')
                print('-'*20)
                result = 'vitoria'
                cont += 1
            else:
                print(f'\nVocê perdeu!')
                print('-'*20)
                result = 'derrota'
                break
        elif escolha == "I":
            if total % 2 == 0:
                print(f'\nVocê perdeu!')
                print('-'*20)
                result = 'derrota'
                break
            else:
                print(f'\nParabéns! Você venceu!')
                print('-'*20)
                result = 'vitoria'
                cont += 1
    if cont > 1:
        print(f'\nVocê conseguiu {cont} vitórias consecutivas.')
    elif cont == 1:
        print(f'\nVocê conseguiu apenas {cont} vitória.')
    else:
        print('\nVocê não conseguiu nenhuma vitória!')
    print('\nFim do Jogo')