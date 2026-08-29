distancia = float(input('Quantos Km você andou com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
preço = (distancia * 0.15) + (dias * 60)
print('Você ficou com o carro {} dia(s) e percorreu {:.2f}Km, o valor total é {:.2f}'.format(dias, distancia, preço))
