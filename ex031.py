viagem = int(input('Qual a distância da sua viagem (em Km)? '))

if viagem <= 200:
    print('O valor da passagem é {}'.format(viagem * 0.50))
else:
    print('O valor da viagem é {}'.format(viagem * 0.45)) 
    