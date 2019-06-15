valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Será pago em quantos anos?: '))
mensal = anos * 12
prestacao = valor / mensal
if prestacao > (salario * 0.30):
    print('Empréstimo negado, a prestação excede o limite permitido')
else:
    print('Empréstimo permitido. Prestação no valor de: R${:.2f}'.format(prestacao))
