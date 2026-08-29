produto = float(input('Insira o valor do produto:R$ '))
desconto = produto - (produto * 5 / 100)
print('O valor original do produto é R${} e seu valor com o desconto de 5% é de R%{}'.format(produto, desconto))
