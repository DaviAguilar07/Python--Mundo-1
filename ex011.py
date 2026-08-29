altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))
area = altura * largura
print('A sua parede tem a dimensão de {}x{} e sua área é de {} m²'.format(altura, largura, area))
tinta = area / 2
print('A quantidade de tinta necessária para pintar a parede é {} L'. format(tinta))
