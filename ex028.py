import random
print('---Jogo de adivinhação---')

print('A máquina escolheu um número de 0 a 5')
sorteio = random.randint(0, 5)

palpite = int(input('Faça um palpite de qual número a máquina escolheu: '))

if palpite == sorteio:
    print('Você acertou!')
else:
    print('O número escolhido pela máquina foi {}\nVocê escolheu {}.\nVocê errou.'.format(sorteio, palpite))
print('---Fim---')
