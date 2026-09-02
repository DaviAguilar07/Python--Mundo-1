velocidade = int(input('Qual a sua velocidade (em Km/h)? '))

if velocidade > 80:
    print('Você está multado em R$ {}.'.format((velocidade - 80) * 7))
else:
    print('Você está seguindo as regras da via.')

