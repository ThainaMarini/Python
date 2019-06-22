from random import randint
n1 = 1
soma = 0
win = 0
qtde = 0
print('Vamos jogar par ou ímpar ;)')
print('Você começa!')
while n1 == 1:
    tipo = str(input('Par ou Ímpar? ')).lower()
    user = int(input('Número: '))
    pc = randint(0, 11)
    if user > 10:
        print('Valor inválido')
        user = int(input('Número: '))
    if tipo == 'par':
        soma = user + pc
        if soma % 2 == 0:
            n1 = 1
            win = win + 1
            qtde = qtde + 1
            print('Você ganhou!')
            print('Vamos denovo!')
        else:
            qtde = qtde + 1
            print('O meu número era {}!'.format(pc))
            print('Você perdeu!')
            n1 = 0
    if (tipo == 'impar') or (tipo == 'ímpar'):
        soma = user + pc
        if soma % 2 != 0:
            print('Você ganhou!')
            print('Vamos denovo!')
            n1 = 1
        else:
            qtde = qtde + 1
            print('O meu número era {}!'.format(pc))
            print('Você perdeu!')
            n1 = 0
print('Foram jogadas {} partida(s)'.format(qtde))
print('Você ganhou {} partida(s)'.format(win))