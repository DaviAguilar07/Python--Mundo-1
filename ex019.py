import random
n1 = str(input('Qual o seu nome? '))
n2 = str(input('Qual o seu nome? '))
n3 = str(input('Qual o seu nome? '))
n4 = str(input('Qual o seu nome? '))
nomes = [n1, n2, n3, n4]

print('O aluno escolhido para apresentar foi: {}'.format(random.choice(nomes)))
