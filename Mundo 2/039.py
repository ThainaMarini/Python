n1 = int(input('Digite seu ano de nascimento: '))
idade = 2019-n1
if idade>=19:
    print('Já passou {} ano(s) do tempo de alistamento'.format(idade-18))
elif idade==18:
    print('É hora de se alistar!')
else:
    print('Você ainda irá se alistar, em {} ano(s)'.format(18-idade))
