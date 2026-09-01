nome = str(input('Insira o seu nome completo: ')).strip().capitalize()

n = nome.split()

print('O seu primeiro nome é {} e o seu último nome é {}'.format(n[0], n[len(n) - 1]))
