#importando as libs
import random
import time

opcoes=['sim', 'nao', 'talvez', 'com certeza', 'nao sei', 'definitivamente sim', 'definitivamente nao',"provavelmente sim",
    'provavelmente nao', 'nao conte com isso', 'melhor nao responder', 'nao tenho certeza', 'pode ser', 'nao posso dizer agora', 'tente novamente mais tarde']
print('Bem-vindo à Bola 8 Mágica!DIgite sua pergunta:')
input('Digite "sair" para encerrar o jogo.\n')
input('Digite sua pergunta: ')
print('A Bola 8 Mágica está pensando...')
while True:
    pergunta = input()
    if pergunta.lower() == 'sair':
        print('Obrigado por jogar! Até a próxima!')
        break
    else:
        print('Pensando...')
        time.sleep(1)  # Simula um tempo de espera para resposta
        resposta = random.choice(opcoes)
        print(f'A Bola 8 Mágica diz: {resposta}')