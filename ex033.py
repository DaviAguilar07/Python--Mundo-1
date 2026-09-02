num1 = float(input('Qual o primeiro número escolhido? '))
num2 = float(input("Qual o segundo número escolhido? "))
num3 = float(input('Qual o terceiro número escolhido? '))

#Verificando quem é o maior:
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

#Verificando quem é o menor:
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O maior número é {:.2f}\nO menor número é {:.2f}'.format(maior, menor))
