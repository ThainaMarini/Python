n1 = float(input('Digite o salário do funcionário: R$'))
if n1>1250:
    print('O novo salário é: R${:.2f}'.format(n1+(n1*0.10)))
else:
    print('O novo salário é: R${:.2f}'.format(n1+(n1*0.15)))