n1 = str(input('Digite o sexo da pessoa: ')).upper()
while n1 not in 'MF':
    n1 = str(input('Valores incorretos. Digite novamente (F/M): ')).upper()
