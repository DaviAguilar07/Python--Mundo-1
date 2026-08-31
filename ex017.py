import math
catoposto = float(input('Qual o valor do cateto oposto? '))
catadjacente = float(input('Qual o valor do cateto adjacente? '))
print('O valor do cateto oposto é {:.2f}, o valor do cateto adjacente é {:.2f}, o valor da hipotenusa é {:.2f}'.format(catoposto, catadjacente, math.hypot(catoposto, catadjacente)))