import random

jogadas = ['pedra', 'papel', 'tesoura']

IA = random.choice(jogadas)

jogador = str(input('Escolha entre pedra, papel e tesoura:')).strip().lower()

if jogador not in jogadas:
    print('invalido')
else:
    print('computador escolheu',IA)

if jogador == IA:
    print('Empate')
elif(
    (jogador == 'pedra' and IA == 'tesoura') or
    ( jogador == 'papel' and IA == 'pedra') or
    ( jogador == 'tesoura' and IA == 'papel') 
    ):
    print('Vc ganhou !!!')
else:
    print('Vc perdeu, que pena')     
Adiciona script principal em Python
