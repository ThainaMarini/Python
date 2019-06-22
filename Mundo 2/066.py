n1 = 1
qtde = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um número inteiro: '))
    if n1 != 999:
        qtde = qtde + 1
        soma = soma + n1
print('Foram digitados {} números.'.format(qtde))
print('A soma desses números é: {}'.format(soma))