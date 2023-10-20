
from random import choice
from time import sleep
from os import system, name

if name == 'nt':  
    cmd = 'cls'
else:  
    cmd = 'clear'

system(cmd)

print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')

def jokenpo():

    jogadas = ['PEDRA' , 'PAPEL' , 'TESOURA']

    print('Escolha: [PEDRA] ou [PAPEL] ou [TESOURA]\n')

    player = input('Faça a sua jogada: ').upper()
    print()

    system(cmd)
    print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')

    if player in jogadas:

        sleep(1)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        sleep(1)

        system(cmd)
        print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')
        print(f'Você jogou {player}!\n')

        pc = choice(jogadas)
        print(f'E o seu adversário jogou {pc}! ', end='')

        if player == 'PEDRA' and pc == 'PEDRA':
            print('Deu empate!')

        elif player == 'PEDRA' and pc == 'PAPEL':
            print('Você perdeu!')

        elif player == 'PEDRA' and pc == 'TESOURA':    
            print('Você venceu!')

        elif player == 'PAPEL' and pc == 'PEDRA':
            print('Você venceu!')

        elif player == 'PAPEL' and pc == 'PAPEL':
            print('Deu empate!')

        elif player == 'PAPEL' and pc == 'TESOURA': 
            print('Você perdeu!')

        elif player == 'TESOURA' and pc == 'PEDRA':
            print('Você perdeu!')

        elif player == 'TESOURA' and pc == 'PAPEL':
            print('Você venceu!')

        elif player == 'TESOURA' and pc == 'TESOURA':
            print('Deu empate!')

        restart()

    else:
        system(cmd)
        print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')
        print('ERRO: Jogada inválida! Tente novamente.\n')
        jokenpo()

def restart():
    print()
    respostassim = ['SIM' , 'S']
    respostasnao = ['NÃO' , 'NAO' , 'N']
    start = input('Quer jogar novamente? S ou N? ').upper()

    if start in respostassim:
        system(cmd)
        print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')
        jokenpo()

    elif start in respostasnao:
        system(cmd)
        print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')
        print('Foi bom jogar com você. Até a próxima! :)\n')
        print('PROGRAMADO POR: Yalle Rocha Silva')
        print('=' * 41)

    else:
        system(cmd)
        print('=' * 10 + ' VAMOS JOGAR JOKENPÔ ' + '=' * 10 + '\n')
        print('ERRO: resposta inválida! Tente novamente.')
        restart()

jokenpo()