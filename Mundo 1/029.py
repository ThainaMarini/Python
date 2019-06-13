n1 = int(input('Digite a velocidade do carro: '))
if n1>80:
    acima= n1-80
    print('Velocidade ultrapassada. Multa no valor de R${:.2f}'.format(acima*7))
else:
    print('Velocidade permitida')