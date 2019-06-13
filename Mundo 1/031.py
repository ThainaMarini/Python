n1 = float(input('Digite a distância da viagem em km: '))
if n1<=200:
    print('O valor da passagem será R${:.2f}'.format(n1*0.50))
else:
    print('O valor da passagem será R${:.2f}'.format(n1*0.45))