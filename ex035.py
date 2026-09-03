reta1 = float(input('Qual o tamanho da primeira reta? '))
reta2 = float(input('Qual o tamanho da segunda reta? '))
reta3 = float(input('Qual o tamanho da terceira reta? '))

if  reta3 < reta1 + reta2 and reta1 < reta2 + reta3 and reta2 < reta3 + reta1:
   print("As retas inseridas podem formar um triângulo.")
else:
   print('As retas inseridas não formam um triângulo.')
