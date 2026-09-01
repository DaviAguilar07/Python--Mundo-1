cidade = str(input('Qual o nome da sua cidade? ')).strip().capitalize()
separador = cidade.split()

print('O nome da sua cidade começa com o nome "Santo": ', 'Santo' in separador[0])
