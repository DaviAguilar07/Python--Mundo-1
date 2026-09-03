salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    print('Você terá um aumento de 10%, dessa maneira o seu salário ficará R$ {:.2f}'.format((salario * 0.10) + salario))
else:
    print('Você terá um aumento de 15%, dessa maneira o seu salário ficará R$ {:.2f}'.format((salario * 0.15) + salario))
    