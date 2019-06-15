preco = float(input('Digite o preço normal do produto: '))
print('Escolha a condição de pagamento:')
print('A-Dinheiro/Cheque')
print('B-À vista no cartão')
print('C-2x no cartão')
print('D-3x ou mais')
cp = str(input())
if cp=='A':
    print('O valor a ser pago no produto será: R${}'.format(preco-(preco*0.10)))
elif str=='B':
    print('O valor a ser pago no produto será: R${}'.format(preco - (preco * 0.05)))
elif cp=='C':
    print('O valor a ser pago no produto será: R${}'.format(preco))
else:
    print('O valor a ser pago no produto será: R${}'.format(preco + (preco * 0.20)))