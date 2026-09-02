from datetime import date
print('---Começando a análise, para ver se é ano bissexto---')
ano = int(input('Insira algum ano ou digite 0 para saber se o ano atual é bissexto: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
