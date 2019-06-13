km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco1 = dias*60
preco2 = km*0.15
print('O preço pago pelos dias é de RS{} e pelos km percorridos de R${}, tendo um total de {}'.format(preco1,preco2,preco1+preco2))