n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
re = 1
while re != 0:
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior valor')
    print('[4] - Digitar novos números')
    print('[5] - Sair do programa ')
    re = int(input('Escolha a operação: '))
    if re == 1:
        print('A soma dos valores {} e {} é: {}'.format(n1,n2,n1+n2))
    if re == 2:
        print('A multiplicação dos valores {} e {} é: {}'.format(n1,n2,n1*n2))
    if re == 3:
        if n1>n2:
            print('O maior valor de {} e {} é: {}'.format(n1,n2,n1))
        else:
            print('O maior valor de {} e {} é: {}'.format(n1, n2, n2))
    if re == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if re == 5:
        print('Fechando programa')
        exit()
    if (re > 5) or (re < 1):
        print('Valores incorretos. Digite novamente')