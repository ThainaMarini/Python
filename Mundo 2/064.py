soma = 0
qtde = 1
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um número inteiro: '))
    if n1 != 999:
        soma = soma + n1
        qtde = qtde + 1
print('Foi digitado {} termos'.format(qtde))
print('A soma desses termos é: {}'.format(soma))