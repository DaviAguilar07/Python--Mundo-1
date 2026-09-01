nome = str(input('Qual o seu nome completo? ')).strip() 
nome = nome.upper()

print('Seu nome tem {} letras A, e a primeira posição em que ele aparece é {} e a última posição da letra é {}'.format(nome.count('A'), nome.find('A') + 1, nome.rfind('A') + 1))
