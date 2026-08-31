import math 
num = float(input('Insira algum valor de ângulo: '))
print('O cosseno desse ângulo é {:.2f}, o seno desse ângulo é {:.2f}, a tangente desse ângulo é {:.2f}'.format(math.cos(math.radians(num)), math.sin(math.radians(num)), math.tan(math.radians(num))))
