nome = str(input('Insira seu nome completo: '))
print('Seu nome em maiúsculo: ', nome.upper())
print('Seu nome em minúsculo: ', nome.lower())

print('Letras ao todo (sem considerar espaços): ', len(nome) - nome.count(' '))

#print('Letras no primeiro nome: ', nome.find(' '))
separa = nome.split()
print('Letras no primeiro nome: ', separa[0], len(separa[0]))